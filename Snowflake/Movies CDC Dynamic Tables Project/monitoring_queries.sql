USE DATABASE MOVIES_CDC_DB;
USE SCHEMA MOVIES_CDC_SCHEMA;

-- Check task status
SHOW TASKS;

-- Check stream status
SHOW STREAMS;
SELECT SYSTEM$STREAM_HAS_DATA('movie_bookings_stream') AS stream_has_data;

-- Task execution history
SELECT *
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY(TASK_NAME => 'CONSUME_STREAM_TASK'))
ORDER BY SCHEDULED_TIME DESC;

-- Dynamic table refresh history
SELECT *
FROM TABLE(INFORMATION_SCHEMA.DYNAMIC_TABLE_REFRESH_HISTORY(TABLE_NAME => 'MOVIE_BOOKINGS_FILTERED'))
ORDER BY REFRESH_START_TIME DESC;

-- Recent CDC events
SELECT *
FROM movie_booking_cdc_events
ORDER BY change_timestamp DESC
LIMIT 20;

-- Revenue summary
SELECT
    status,
    COUNT(*) AS bookings,
    SUM(active_revenue) AS active_revenue,
    SUM(lost_revenue) AS lost_revenue
FROM movie_bookings_filtered
GROUP BY status
ORDER BY bookings DESC;
