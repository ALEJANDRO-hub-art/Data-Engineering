# Databricks notebook source
# Converted from: healthcare_dlt_processing(1).ipynb

# COMMAND ----------
-- Databricks notebook source
-- =============================================================================
-- HEALTHCARE DLT PIPELINE - BRONZE LAYER: DIAGNOSTIC MAPPING
-- =============================================================================
-- This table creates a bronze layer for diagnosis code mappings
-- Purpose: Reference data for diagnosis codes to descriptions
-- Data Quality: Enforces non-null constraints on critical fields
-- Violation Handling: Drops rows with null diagnosis codes or descriptions

CREATE LIVE TABLE diagnostic_mapping(
  -- Data Quality Constraints: Ensure critical fields are not null
  CONSTRAINT diag_code_not_null EXPECT (diagnosis_code IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT diag_desc_not_null EXPECT (diagnosis_description IS NOT NULL) ON VIOLATION DROP ROW
)
COMMENT "Bronze table for the diagnosis mapping file - Reference data for diagnosis codes"
TBLPROPERTIES ("quality" = "bronze")
AS
SELECT
  -- Explicit type casting for data consistency
  CAST(diagnosis_code AS STRING) AS diagnosis_code,
  CAST(diagnosis_description AS STRING) AS diagnosis_description
FROM gds_de_bootcamp_new.default.raw_diagnosis_map

# COMMAND ----------
-- =============================================================================
-- HEALTHCARE DLT PIPELINE - BRONZE LAYER: DAILY PATIENTS (STREAMING)
-- =============================================================================
-- This table creates a streaming bronze layer for daily patient admissions
-- Purpose: Real-time ingestion of patient data with comprehensive data quality checks
-- Streaming: Uses STREAM() to process new data as it arrives
-- Data Quality: Enforces business rules for patient data completeness

CREATE OR REFRESH STREAMING TABLE daily_patients(
  -- Primary Key Constraint: Patient ID must be present
  CONSTRAINT pk_not_null EXPECT (patient_id IS NOT NULL) ON VIOLATION DROP ROW,
  -- Business Rule: All essential patient fields must be populated
  CONSTRAINT required_fields EXPECT (name IS NOT NULL AND age IS NOT NULL AND gender IS NOT NULL AND address IS NOT NULL AND contact_number IS NOT NULL AND admission_date IS NOT NULL) ON VIOLATION DROP ROW
)
COMMENT "Bronze table for daily patient data - Streaming ingestion with data quality enforcement"
TBLPROPERTIES ("quality" = "bronze")
AS
SELECT
  -- Explicit type casting for data consistency and validation
  CAST(patient_id AS STRING) AS patient_id,
  CAST(name AS STRING) AS name,
  CAST(age AS INT) AS age,
  CAST(gender AS STRING) AS gender,
  CAST(address AS STRING) AS address,
  CAST(contact_number AS STRING) AS contact_number,
  CAST(admission_date AS DATE) AS admission_date,
  CAST(diagnosis_code AS STRING) AS diagnosis_code
FROM STREAM(gds_de_bootcamp_new.default.raw_patients_daily)

# COMMAND ----------
-- =============================================================================
-- HEALTHCARE DLT PIPELINE - SILVER LAYER: PROCESSED PATIENT DATA
-- =============================================================================
-- This table creates a silver layer by joining patient data with diagnosis mappings
-- Purpose: Enriched patient data with human-readable diagnosis descriptions
-- Data Quality: Ensures diagnosis descriptions are available for analysis
-- Join Strategy: LEFT JOIN to preserve all patients, even those with unmapped codes

CREATE OR REFRESH STREAMING TABLE processed_patient_data
  -- Data Quality: Ensure diagnosis description is available for meaningful analysis
  (CONSTRAINT has_diagnosis EXPECT (diagnosis_description IS NOT NULL) ON VIOLATION DROP ROW)
COMMENT "Silver table with enriched patient data - Joined with diagnosis mappings for analysis"
TBLPROPERTIES ("quality" = "silver")
AS
SELECT
    -- Patient demographic and admission information
    p.patient_id,
    p.name,
    p.age,
    p.gender,
    p.address,
    p.contact_number,
    p.admission_date,
    m.diagnosis_description AS diagnosis_description
FROM STREAM(live.daily_patients) p
LEFT JOIN live.diagnostic_mapping m
  ON p.diagnosis_code = m.diagnosis_code;

# COMMAND ----------
-- =============================================================================
-- HEALTHCARE DLT PIPELINE - GOLD LAYER: PATIENT STATISTICS BY ADMISSION DATE
-- =============================================================================
-- This table creates aggregated analytics for daily patient admissions by diagnosis
-- Purpose: Daily operational metrics for hospital capacity and diagnosis trends
-- Aggregation: Groups by admission date and diagnosis for time-series analysis
-- Metrics: Patient counts and average age for demographic insights

CREATE LIVE TABLE patient_statistics_by_admission_date
COMMENT "Gold table with daily patient admission statistics by diagnosis - Operational metrics"
TBLPROPERTIES ("quality" = "gold")
AS
SELECT
  -- Time dimension for trend analysis
  admission_date,
  -- Diagnosis dimension for medical insights
  diagnosis_description,
  -- Key operational metrics
  COUNT(*) AS patient_count,
  AVG(age) AS avg_age
FROM live.processed_patient_data
GROUP BY admission_date, diagnosis_description;

# COMMAND ----------
-- =============================================================================
-- HEALTHCARE DLT PIPELINE - GOLD LAYER: PATIENT STATISTICS BY DIAGNOSIS
-- =============================================================================
-- This table creates comprehensive analytics for each diagnosis type
-- Purpose: Medical insights and demographic analysis by diagnosis
-- Aggregation: Groups by diagnosis for medical research and capacity planning
-- Metrics: Patient counts, age statistics, and gender distribution

CREATE LIVE TABLE patient_statistics_by_diagnosis
COMMENT "Gold table with comprehensive patient statistics by diagnosis - Medical analytics"
TBLPROPERTIES ("quality" = "gold")
AS
SELECT
    -- Diagnosis dimension for medical categorization
    diagnosis_description,
    -- Patient volume metrics
    COUNT(patient_id) AS patient_count,
    -- Age demographic analysis
    AVG(age) AS avg_age,
    MIN(age) AS min_age,
    MAX(age) AS max_age,
    -- Gender distribution analysis
    COUNT(DISTINCT gender) AS unique_gender_count
FROM live.processed_patient_data
GROUP BY diagnosis_description;

# COMMAND ----------
-- =============================================================================
-- HEALTHCARE DLT PIPELINE - GOLD LAYER: PATIENT STATISTICS BY GENDER
-- =============================================================================
-- This table creates demographic analytics grouped by patient gender
-- Purpose: Gender-based health insights and demographic analysis
-- Aggregation: Groups by gender for population health studies
-- Metrics: Patient counts, age statistics, and diagnosis diversity

CREATE LIVE TABLE patient_statistics_by_gender
COMMENT "Gold table with demographic patient statistics by gender - Population health analytics"
TBLPROPERTIES ("quality" = "gold")
AS
SELECT
    -- Gender dimension for demographic analysis
    gender,
    -- Patient volume metrics
    COUNT(patient_id) AS patient_count,
    -- Age demographic analysis
    AVG(age) AS avg_age,
    MIN(age) AS min_age,
    MAX(age) AS max_age,
    -- Medical diversity analysis
    COUNT(DISTINCT diagnosis_description) AS unique_diagnosis_count
FROM live.processed_patient_data
GROUP BY gender;

