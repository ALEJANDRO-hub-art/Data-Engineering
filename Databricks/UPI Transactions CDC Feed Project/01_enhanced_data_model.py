# Converted from: 01_enhanced_data_model(2).ipynb
# Auto-generated Python script from Jupyter Notebook

# %% [markdown] Cell 1
# # =============================================================================
# # UPI TRANSACTIONS CDC FEED PROJECT - ENHANCED DATA MODEL
# # =============================================================================
# # This notebook creates an enhanced data model for UPI transactions with CDC support
# # Purpose: Establishes comprehensive schema for real-time UPI transaction processing
# # Features: CDC-enabled tables, partitioning, auto-optimization, and performance tuning
# # Output: Creates raw transaction table and merchant aggregation table with CDC support

# %% Cell 2
# =============================================================================
# CONFIGURATION SETUP
# =============================================================================
# Configure Unity Catalog and schema for UPI transactions data model
# catalog_name: Unity Catalog name for data governance and management
# schema_name: Target schema for organizing UPI transaction tables

catalog_name = "`gds_de_bootcamp_new`"
schema_name = "default"

print(f"Using catalog: {catalog_name}, schema: {schema_name}")

# %% Cell 3
# =============================================================================
# RAW UPI TRANSACTIONS TABLE WITH CDC SUPPORT
# =============================================================================
# Create comprehensive raw UPI transactions table with Change Data Capture enabled
# Purpose: Store all UPI transaction data with CDC for real-time streaming processing
# Features: CDC feed, auto-optimization, partitioning, and comprehensive transaction schema
# Schema: Includes transaction details, merchant info, customer data, and location data

raw_table_sql = f"""
CREATE TABLE IF NOT EXISTS {catalog_name}.{schema_name}.raw_upi_transactions_v1 (
    -- Transaction Core Fields
    transaction_id STRING NOT NULL,           -- Unique transaction identifier
    upi_id STRING NOT NULL,                   -- UPI ID of the payer
    merchant_id STRING NOT NULL,              -- Merchant identifier
    merchant_name STRING,                     -- Merchant business name
    merchant_category STRING,                 -- Merchant category for partitioning
    
    -- Transaction Financial Details
    transaction_amount DOUBLE NOT NULL,       -- Transaction amount
    transaction_currency STRING NOT NULL,     -- Currency (INR for India)
    transaction_timestamp TIMESTAMP NOT NULL, -- Transaction timestamp
    transaction_status STRING NOT NULL,       -- Status: completed, failed, initiated, refunded
    payment_method STRING,                    -- Payment method: UPI, QR Code, etc.
    
    -- Device and App Information
    device_type STRING,                       -- Device type: Mobile, Tablet
    device_os STRING,                         -- Operating system: Android, iOS
    app_version STRING,                       -- UPI app version
    
    -- Location Information
    latitude DOUBLE,                          -- Transaction location latitude
    longitude DOUBLE,                         -- Transaction location longitude
    city STRING,                              -- City name
    state STRING,                             -- State name
    country STRING,                           -- Country name
    
    -- Customer Demographics
    customer_id STRING,                       -- Customer identifier
    age_group STRING,                         -- Age group: 18-25, 26-35, etc.
    gender STRING,                            -- Gender: Male, Female, Other
    
    -- Financial Calculations
    processing_fee DOUBLE,                    -- Processing fee charged
    commission DOUBLE,                        -- Commission earned
    
    -- Audit Fields
    created_at TIMESTAMP,                     -- Record creation timestamp
    updated_at TIMESTAMP                      -- Record last update timestamp
) 
USING DELTA
TBLPROPERTIES (
    'delta.enableChangeDataFeed' = true,      -- Enable CDC for streaming
    'delta.autoOptimize.optimizeWrite' = true, -- Auto-optimize writes
    'delta.autoOptimize.autoCompact' = true   -- Auto-compact small files
)
PARTITIONED BY (merchant_category)            -- Partition by merchant category for performance
"""

spark.sql(raw_table_sql)
print("Enhanced raw UPI transactions table created with CDC enabled")

# %% Cell 4
# =============================================================================
# MERCHANT AGGREGATION TABLE
# =============================================================================
# Create merchant aggregation table for real-time merchant performance analytics
# Purpose: Store hourly aggregated merchant metrics for business intelligence
# Features: Auto-optimization, partitioning, and comprehensive merchant KPIs
# Schema: Includes transaction counts, amounts, success rates, and customer metrics

merchant_agg_sql = f"""
CREATE TABLE IF NOT EXISTS {catalog_name}.{schema_name}.merchant_aggregations (
    -- Merchant Identification
    merchant_id STRING NOT NULL,              -- Merchant identifier
    merchant_name STRING,                     -- Merchant business name
    merchant_category STRING,                 -- Merchant category for partitioning
    
    -- Time Dimensions
    aggregation_date DATE NOT NULL,           -- Date of aggregation
    aggregation_hour TIMESTAMP,               -- Hour of aggregation for time-series analysis
    
    -- Transaction Count Metrics
    total_transactions BIGINT,                -- Total number of transactions
    successful_transactions BIGINT,           -- Number of successful transactions
    failed_transactions BIGINT,               -- Number of failed transactions
    refunded_transactions BIGINT,             -- Number of refunded transactions
    
    -- Transaction Amount Metrics
    total_transaction_amount DOUBLE,          -- Total transaction amount
    successful_transaction_amount DOUBLE,     -- Amount from successful transactions
    failed_transaction_amount DOUBLE,         -- Amount from failed transactions
    refunded_transaction_amount DOUBLE,       -- Amount from refunded transactions
    net_transaction_amount DOUBLE,            -- Net amount after refunds
    
    -- Financial Metrics
    total_processing_fee DOUBLE,              -- Total processing fees collected
    total_commission DOUBLE,                  -- Total commission earned
    
    -- Performance Metrics
    success_rate DOUBLE,                      -- Success rate percentage
    unique_customers BIGINT,                  -- Number of unique customers
    
    -- Time Range Metrics
    first_transaction_timestamp TIMESTAMP,    -- First transaction in the period
    last_transaction_timestamp TIMESTAMP,     -- Last transaction in the period
    
    -- Audit Fields
    created_at TIMESTAMP,                     -- Record creation timestamp
    updated_at TIMESTAMP                      -- Record last update timestamp
) 
USING DELTA
TBLPROPERTIES (
    'delta.autoOptimize.optimizeWrite' = true, -- Auto-optimize writes
    'delta.autoOptimize.autoCompact' = true   -- Auto-compact small files
)
PARTITIONED BY (merchant_category)            -- Partition by merchant category for performance
"""

spark.sql(merchant_agg_sql)
print("Merchant aggregations table created")
