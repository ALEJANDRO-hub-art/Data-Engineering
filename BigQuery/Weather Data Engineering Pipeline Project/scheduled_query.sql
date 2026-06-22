-- Run this query before scheduling aggregate query

CREATE TABLE IF NOT EXISTS `mythic-aloe-457912-d5.telecom_db.daily_call_summary` (
  summary_date    DATE,
  region          STRING,
  plan_type       STRING,
  total_calls     INT64,
  total_duration  INT64,
  avg_duration    FLOAT64,
  total_data_mb   FLOAT64,
  avg_data_mb     FLOAT64
)
PARTITION BY summary_date
OPTIONS (
  description = "Daily telecom call summary by region & plan",
  labels = [("env","dev"),("source","telecom_calls")],
  require_partition_filter = TRUE
);

-- Aggregate query for scheduling

SELECT
  DATE(call_date)             AS summary_date,
  region,
  plan_type,
  COUNT(*)                    AS total_calls,
  SUM(duration_seconds)       AS total_duration,
  AVG(duration_seconds)       AS avg_duration,
  SUM(data_usage_mb)          AS total_data_mb,
  AVG(data_usage_mb)          AS avg_data_mb
FROM
  `mythic-aloe-457912-d5.telecom_db.telecom_calls`
WHERE
  DATE(call_date) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
GROUP BY
  summary_date, region, plan_type;