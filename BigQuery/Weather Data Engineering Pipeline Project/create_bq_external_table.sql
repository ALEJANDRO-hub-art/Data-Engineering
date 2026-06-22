-- Create schema in dataset
CREATE SCHEMA IF NOT EXISTS `mythic-aloe-457912-d5.lyft_db`;

-- Create external table
CREATE EXTERNAL TABLE `mythic-aloe-457912-d5.lyft_db.lyft_rides_ext` (
  ride_id        STRING,
  user_id        STRING,
  driver_id      STRING,
  start_location STRUCT<latitude FLOAT64, longitude FLOAT64>,
  end_location   STRUCT<latitude FLOAT64, longitude FLOAT64>,
  start_time     TIMESTAMP,
  end_time       TIMESTAMP,
  distance_miles FLOAT64,
  price_usd      FLOAT64
)
WITH PARTITION COLUMNS (
  date           DATE    -- auto-extracted from the folder name
)
OPTIONS (
  format                              = 'NEWLINE_DELIMITED_JSON',
  uris                                = ['gs://bigquery-data-gds/raw/date=*'],
  hive_partition_uri_prefix = 'gs://bigquery-data-gds/raw/'
);

-- Check distinct partitions created
SELECT
  DISTINCT date
FROM
  `mythic-aloe-457912-d5.lyft_db.lyft_rides_ext`
ORDER BY
  date DESC;

-- Query Data
Select * from `mythic-aloe-457912-d5.lyft_db.lyft_rides_ext` where date = '2025-05-10'

