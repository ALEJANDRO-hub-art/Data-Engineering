-- =============================================================
-- Test CDC behavior after running snowflake_dynamic_tables.sql
-- =============================================================
USE DATABASE MOVIES_CDC_DB;
USE SCHEMA MOVIES_CDC_SCHEMA;
USE WAREHOUSE COMPUTE_WH;

-- 1) Insert a new booking
INSERT INTO raw_movie_bookings
    (booking_id, customer_id, movie_id, booking_date, status, ticket_count, ticket_price)
VALUES
    ('B006', 'C006', 'M001', '2025-09-05 20:30:00', 'BOOKED', 5, 18.00);

-- 2) Update an existing booking to CANCELLED
UPDATE raw_movie_bookings
SET status = 'CANCELLED',
    updated_at = CURRENT_TIMESTAMP()
WHERE booking_id = 'B002';

-- 3) Delete a booking
DELETE FROM raw_movie_bookings
WHERE booking_id = 'B004';

-- 4) Force the task to consume the stream immediately
EXECUTE TASK consume_stream_task;

-- 5) Refresh dynamic tables manually if you do not want to wait for target lag
ALTER DYNAMIC TABLE movie_bookings_filtered REFRESH;
ALTER DYNAMIC TABLE movie_booking_insights REFRESH;

-- 6) Check results
SELECT * FROM movie_booking_cdc_events ORDER BY change_timestamp DESC;
SELECT * FROM movie_bookings_filtered ORDER BY change_timestamp DESC;
SELECT * FROM movie_booking_insights ORDER BY active_revenue DESC;
