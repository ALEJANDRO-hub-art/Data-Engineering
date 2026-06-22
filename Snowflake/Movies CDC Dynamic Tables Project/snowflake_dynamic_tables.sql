-- =============================================================
-- Movies CDC Dynamic Tables Project
-- Snowflake Streams + Tasks + Dynamic Tables + Streamlit Dashboard
-- =============================================================

-- 1) Create database and schema
CREATE DATABASE IF NOT EXISTS MOVIES_CDC_DB;
USE DATABASE MOVIES_CDC_DB;

CREATE SCHEMA IF NOT EXISTS MOVIES_CDC_SCHEMA;
USE SCHEMA MOVIES_CDC_SCHEMA;

-- Change this warehouse if your Snowflake warehouse has another name.
USE WAREHOUSE COMPUTE_WH;

-- 2) Source table: raw movie bookings
CREATE OR REPLACE TABLE raw_movie_bookings (
    booking_id STRING,
    customer_id STRING,
    movie_id STRING,
    booking_date TIMESTAMP_NTZ,
    status STRING,
    ticket_count INT,
    ticket_price NUMBER(10, 2),
    total_amount NUMBER(10, 2) AS (ticket_count * ticket_price),
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
    updated_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

-- 3) Insert sample data
INSERT INTO raw_movie_bookings
    (booking_id, customer_id, movie_id, booking_date, status, ticket_count, ticket_price)
VALUES
    ('B001', 'C001', 'M001', '2025-09-01 10:15:00', 'BOOKED', 2, 15.00),
    ('B002', 'C002', 'M002', '2025-09-01 11:30:00', 'BOOKED', 1, 25.00),
    ('B003', 'C003', 'M003', '2025-09-02 13:45:00', 'CANCELLED', 4, 12.50),
    ('B004', 'C004', 'M004', '2025-09-03 17:20:00', 'BOOKED', 3, 10.00),
    ('B005', 'C005', 'M005', '2025-09-04 19:00:00', 'BOOKED', 1, 22.00);

-- 4) Stream: captures INSERT, UPDATE, DELETE changes from source table
CREATE OR REPLACE STREAM movie_bookings_stream
ON TABLE raw_movie_bookings
SHOW_INITIAL_ROWS = TRUE;

-- 5) CDC events table: stores stream rows plus CDC metadata
CREATE OR REPLACE TABLE movie_booking_cdc_events (
    booking_id STRING,
    customer_id STRING,
    movie_id STRING,
    booking_date TIMESTAMP_NTZ,
    status STRING,
    ticket_count INT,
    ticket_price NUMBER(10, 2),
    total_amount NUMBER(10, 2),
    created_at TIMESTAMP_NTZ,
    updated_at TIMESTAMP_NTZ,
    change_action STRING,
    is_update BOOLEAN,
    change_timestamp TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

-- 6) Task: consumes stream data every minute
CREATE OR REPLACE TASK consume_stream_task
    WAREHOUSE = COMPUTE_WH
    SCHEDULE = '1 MINUTE'
    WHEN SYSTEM$STREAM_HAS_DATA('movie_bookings_stream')
AS
INSERT INTO movie_booking_cdc_events (
    booking_id,
    customer_id,
    movie_id,
    booking_date,
    status,
    ticket_count,
    ticket_price,
    total_amount,
    created_at,
    updated_at,
    change_action,
    is_update,
    change_timestamp
)
SELECT
    booking_id,
    customer_id,
    movie_id,
    booking_date,
    status,
    ticket_count,
    ticket_price,
    total_amount,
    created_at,
    updated_at,
    METADATA$ACTION AS change_action,
    METADATA$ISUPDATE AS is_update,
    CURRENT_TIMESTAMP() AS change_timestamp
FROM movie_bookings_stream;

-- Start the task
ALTER TASK consume_stream_task RESUME;

-- Run once manually so initial rows from SHOW_INITIAL_ROWS are consumed immediately.
EXECUTE TASK consume_stream_task;

-- 7) Dynamic table: detailed filtered/enriched booking data
CREATE OR REPLACE DYNAMIC TABLE movie_bookings_filtered
    TARGET_LAG = '2 MINUTES'
    WAREHOUSE = COMPUTE_WH
AS
SELECT
    booking_id,
    customer_id,
    movie_id,
    booking_date,
    status,
    ticket_count,
    ticket_price,
    total_amount,
    created_at,
    updated_at,
    change_action,
    is_update,
    change_timestamp,

    CASE
        WHEN status = 'BOOKED' THEN 'ACTIVE'
        WHEN status = 'CANCELLED' THEN 'INACTIVE'
        ELSE 'UNKNOWN'
    END AS booking_status_category,

    CASE
        WHEN ticket_count = 1 THEN 'SINGLE'
        WHEN ticket_count BETWEEN 2 AND 4 THEN 'GROUP'
        WHEN ticket_count >= 5 THEN 'LARGE_GROUP'
        ELSE 'UNKNOWN'
    END AS booking_size_category,

    CASE
        WHEN ticket_price < 10 THEN 'BUDGET'
        WHEN ticket_price BETWEEN 10 AND 20 THEN 'STANDARD'
        WHEN ticket_price > 20 THEN 'PREMIUM'
        ELSE 'UNKNOWN'
    END AS price_category,

    CASE WHEN status = 'BOOKED' THEN total_amount ELSE 0 END AS active_revenue,
    CASE WHEN status = 'CANCELLED' THEN total_amount ELSE 0 END AS lost_revenue,

    CASE
        WHEN booking_id IS NULL OR customer_id IS NULL OR movie_id IS NULL THEN FALSE
        WHEN ticket_count <= 0 OR ticket_price <= 0 THEN FALSE
        WHEN status NOT IN ('BOOKED', 'CANCELLED') THEN FALSE
        ELSE TRUE
    END AS is_valid_booking,

    EXTRACT(HOUR FROM booking_date) AS booking_hour,
    DAYNAME(booking_date) AS booking_day_name,
    TO_DATE(booking_date) AS booking_day
FROM movie_booking_cdc_events
WHERE booking_id IS NOT NULL
  AND customer_id IS NOT NULL;

-- 8) Dynamic table: aggregated insights for dashboard
CREATE OR REPLACE DYNAMIC TABLE movie_booking_insights
    TARGET_LAG = DOWNSTREAM
    WAREHOUSE = COMPUTE_WH
AS
SELECT
    movie_id,
    status,
    booking_status_category,
    booking_size_category,
    price_category,
    COUNT(*) AS total_bookings,
    SUM(ticket_count) AS total_tickets,
    SUM(total_amount) AS gross_amount,
    SUM(active_revenue) AS active_revenue,
    SUM(lost_revenue) AS lost_revenue,
    ROUND(AVG(ticket_price), 2) AS avg_ticket_price,
    ROUND(100 * AVG(IFF(is_valid_booking, 1, 0)), 2) AS data_quality_score,
    COUNT_IF(change_action = 'INSERT') AS insert_events,
    COUNT_IF(change_action = 'DELETE') AS delete_events,
    COUNT_IF(is_update) AS update_events,
    MIN(booking_date) AS first_booking_date,
    MAX(booking_date) AS latest_booking_date,
    MAX(change_timestamp) AS latest_change_timestamp
FROM movie_bookings_filtered
GROUP BY
    movie_id,
    status,
    booking_status_category,
    booking_size_category,
    price_category;

-- 9) Helpful verification commands
SHOW TABLES;
SHOW STREAMS;
SHOW TASKS;
SHOW DYNAMIC TABLES;

SELECT * FROM movie_booking_cdc_events ORDER BY change_timestamp DESC;
SELECT * FROM movie_bookings_filtered ORDER BY change_timestamp DESC;
SELECT * FROM movie_booking_insights ORDER BY active_revenue DESC;
