-- Create schema in dataset

CREATE SCHEMA IF NOT EXISTS `mythic-aloe-457912-d5.telecom_db`;


-- Create tabel in a schema
CREATE TABLE IF NOT EXISTS `mythic-aloe-457912-d5.telecom_db.telecom_calls` (
  call_id          STRING,
  customer_id      STRING,
  call_date        TIMESTAMP,
  duration_seconds INT64,
  call_type        STRING,
  data_usage_mb    FLOAT64,
  region           STRING,
  plan_type        STRING
)
PARTITION BY DATE(call_date)
CLUSTER BY region, plan_type
OPTIONS (
  description = "Telecom call logs, partitioned by call_date, clustered by region & plan_type",
  labels = [("env","dev"),("source","csv")],
  require_partition_filter = FALSE
);

-- Load data from Google storage
LOAD DATA INTO `mythic-aloe-457912-d5.telecom_db.telecom_calls`
FROM FILES (
  format = 'CSV',
  uris = ['gs://bigquery-data-gds/telecom_data/telecom_data.csv'],
  skip_leading_rows = 1,
  field_delimiter = ',',
  max_bad_records = 50
);


-- Insert data manually
INSERT INTO `mythic-aloe-457912-d5.telecom_db.telecom_calls` (
  call_id, customer_id, call_date, duration_seconds,
  call_type, data_usage_mb, region, plan_type
)
VALUES
  ('CALL999999','CUST1234','2025-05-09 14:22:00', 300,'Voice',12.5,'North','Standard'),
  ('CALL1000000','CUST2234','2025-05-09 15:10:00', 45,'SMS',0.0,'East','Basic');

-- Read data with parition column
SELECT *
FROM `mythic-aloe-457912-d5.telecom_db.telecom_calls`
WHERE DATE(call_date) = '2025-05-09';

-- Update record in BQ Table
UPDATE `mythic-aloe-457912-d5.telecom_db.telecom_calls`
SET plan_type = 'Premium'
WHERE customer_id = 'CUST1234';

-- Delete record from BQ Table
DELETE FROM `mythic-aloe-457912-d5.telecom_db.telecom_calls`
WHERE call_id = 'CALL1000000';

-- List of tables present in a schema
SELECT
  table_name
FROM
  `mythic-aloe-457912-d5.telecom_db`.INFORMATION_SCHEMA.TABLES;


-- Get details of a table
SELECT
  column_name,
  data_type,
  is_nullable,
  generation_expression
FROM
  `mythic-aloe-457912-d5.telecom_db`.INFORMATION_SCHEMA.COLUMNS
WHERE
  table_name = 'telecom_calls'
ORDER BY
  ordinal_position;

-- Read using BigQuery Time Travel Feature
SELECT *
FROM `mythic-aloe-457912-d5.telecom_db.telecom_calls`
FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 15 MINUTE);

-- Get list of partitions
SELECT
  *
FROM
  `mythic-aloe-457912-d5.telecom_db.INFORMATION_SCHEMA.PARTITIONS`
WHERE
  table_name = 'telecom_calls'
ORDER BY
  partition_id DESC;

-- When you declare PARTITION BY DATE(call_date)
-- BigQuery under the covers does two things:
--	1.	Creates one partition per calendar date (e.g. “2025-05-09”), which it internally labels as the string 20250509 (no dashes).
--	2.	Exposes a hidden pseudo-column called _PARTITIONDATE of type DATE that holds that same date.

-- When you run
-- SELECT * 
-- FROM mydataset.telecom_calls
-- WHERE DATE(call_date) = '2025-05-09';

-- BigQuery’s optimizer recognizes that you’re filtering on the partitioning column and rewrites your query to only scan the single partition whose internal ID is 20250509. It does this by:
-- 	•	Casting your literal '2025-05-09' to a DATE.
-- 	•	Matching it against _PARTITIONDATE.
-- 	•	Translating that to the partition named telecom_calls$20250509.