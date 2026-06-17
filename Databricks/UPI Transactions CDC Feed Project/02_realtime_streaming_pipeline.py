# Converted from: 02_realtime_streaming_pipeline(2).ipynb
# Auto-generated Python script from Jupyter Notebook

# %% [markdown] Cell 1
# # =============================================================================
# # UPI TRANSACTIONS CDC FEED PROJECT - REAL-TIME STREAMING PIPELINE
# # =============================================================================
# # This notebook implements a real-time streaming pipeline for UPI transaction processing
# # Purpose: Processes UPI transactions in real-time using CDC and structured streaming
# # Features: CDC-aware processing, merchant aggregations, error handling, and monitoring
# # Output: Real-time merchant performance metrics and transaction analytics

# %% Cell 2
# =============================================================================
# LIBRARY IMPORTS AND CONFIGURATION
# =============================================================================
# Import required libraries for real-time streaming and CDC processing
# Purpose: Set up environment for structured streaming, Delta operations, and data processing

from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.streaming import StreamingQuery
from delta.tables import DeltaTable
from datetime import datetime, timedelta
import uuid

# =============================================================================
# CONFIGURATION SETUP
# =============================================================================
# Configure Unity Catalog and table names for streaming pipeline
# catalog_name: Unity Catalog for data governance
# schema_name: Target schema for UPI transaction tables
# raw_table: Source table with CDC enabled for streaming
# merchant_agg_table: Target table for merchant aggregations

catalog_name = "`gds_de_bootcamp_new`"
schema_name = "default"

# Table names
raw_table = f"{catalog_name}.{schema_name}.raw_upi_transactions_v1"
merchant_agg_table = f"{catalog_name}.{schema_name}.merchant_aggregations"

print("Libraries imported and configuration set")
print(f"Target tables: {raw_table}, {merchant_agg_table}")

# %% Cell 3
# =============================================================================
# DELTA TABLE MERGE FUNCTION
# =============================================================================
# Implements idempotent merge operation for merchant aggregations
# Purpose: Ensures data consistency and handles upsert operations efficiently
# Features: Uses Delta Lake merge for ACID transactions and conflict resolution

def merge_to_delta_table(delta_table_name: str, batch_df):
    """
    Idempotent merge function for Delta tables
    
    Args:
        delta_table_name: Name of the target Delta table
        batch_df: DataFrame containing data to merge
    
    Business Logic:
        - Merges on merchant_id, aggregation_date, and aggregation_hour
        - Updates existing records with new values
        - Inserts new records for new merchant/date/hour combinations
    """
    delta_table = DeltaTable.forName(spark, delta_table_name)
    
    # Perform merge operation with composite key
    delta_table.alias("target").merge(
        batch_df.alias("source"),
        "target.merchant_id = source.merchant_id AND target.aggregation_date = source.aggregation_date AND target.aggregation_hour = source.aggregation_hour"
    ).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()

print("Delta table merge function defined")

# %% Cell 4
# Simple merchant aggregation function with CDC-aware logic
def process_merchant_aggregations(batch_df, batch_id):
    """Process merchant aggregations using CDC-aware approach"""
    try:
        print(f"Processing batch {batch_id} with {batch_df.count()} records")
        
        # Only consider records with required fields
        filtered_df = batch_df.filter(
            (F.col("transaction_id").isNotNull()) &
            (F.col("merchant_id").isNotNull()) &
            (F.col("transaction_amount").isNotNull()) &
            (F.col("transaction_amount") > 0) &
            (F.col("transaction_timestamp").isNotNull()) &
            (F.col("transaction_status").isNotNull()) &
            (F.col("_change_type").isin("insert", "delete"))
        )
        
        if filtered_df.count() == 0:
            print("No valid records found in batch")
            return

        # Assign +1 for insert, -1 for delete for counting
        cdc_df = filtered_df.withColumn(
            "cdc_multiplier",
            F.when(F.col("_change_type").isin("insert"), F.lit(1))
             .when(F.col("_change_type").isin("delete"), F.lit(-1))
             .otherwise(F.lit(0))
        )

        # For delete, we want to "remove" the record
        # For insert, we want to "add" the record

        # Prepare aggregation columns with CDC logic
        merchant_aggregations = cdc_df.groupBy(
            F.col("merchant_id"),
            F.col("merchant_name"),
            F.col("merchant_category"),
            F.date_trunc("hour", F.col("transaction_timestamp")).cast("timestamp").alias("aggregation_hour"),
            F.to_date(F.col("transaction_timestamp")).alias("aggregation_date")
        ).agg(
            (F.sum(F.col("cdc_multiplier"))).alias("total_transactions"),
            (F.sum(F.when(F.col("transaction_status") == "completed", F.col("cdc_multiplier")).otherwise(0))).alias("successful_transactions"),
            (F.sum(F.when(F.col("transaction_status") == "failed", F.col("cdc_multiplier")).otherwise(0))).alias("failed_transactions"),
            (F.sum(F.when(F.col("transaction_status") == "refunded", F.col("cdc_multiplier")).otherwise(0))).alias("refunded_transactions"),
            
            (F.sum(F.col("transaction_amount") * F.col("cdc_multiplier"))).alias("total_transaction_amount"),
            (F.sum(F.when(F.col("transaction_status") == "completed", F.col("transaction_amount") * F.col("cdc_multiplier")).otherwise(0))).alias("successful_transaction_amount"),
            (F.sum(F.when(F.col("transaction_status") == "failed", F.col("transaction_amount") * F.col("cdc_multiplier")).otherwise(0))).alias("failed_transaction_amount"),
            (F.sum(F.when(F.col("transaction_status") == "refunded", F.col("transaction_amount") * F.col("cdc_multiplier")).otherwise(0))).alias("refunded_transaction_amount"),
            
            (F.sum(F.coalesce(F.col("processing_fee"), F.lit(0)) * F.col("cdc_multiplier"))).alias("total_processing_fee"),
            (F.sum(F.coalesce(F.col("commission"), F.lit(0)) * F.col("cdc_multiplier"))).alias("total_commission"),
            
            (F.countDistinct(F.when(F.col("cdc_multiplier") == 1, F.col("upi_id")))).alias("unique_customers"),
            
            F.min(F.when(F.col("cdc_multiplier") == 1, F.col("transaction_timestamp"))).alias("first_transaction_timestamp"),
            F.max(F.when(F.col("cdc_multiplier") == 1, F.col("transaction_timestamp"))).alias("last_transaction_timestamp")
        )

        # Calculate success rate and net amount
        merchant_aggregations = merchant_aggregations.withColumn(
            "success_rate",
            F.when(F.col("total_transactions") > 0, 
                   (F.col("successful_transactions") / F.col("total_transactions")) * 100)
            .otherwise(0)
        ).withColumn(
            "net_transaction_amount",
            F.col("successful_transaction_amount") - F.col("refunded_transaction_amount")
        ).withColumn(
            "created_at", F.current_timestamp()
        ).withColumn(
            "updated_at", F.current_timestamp()
        )
        
        # Use simple merge function
        merge_to_delta_table(merchant_agg_table, merchant_aggregations)
        
        records_processed = merchant_aggregations.count()
        print(f"Merchant aggregations processed: {records_processed} records")
        
    except Exception as e:
        print(f"Error processing merchant aggregations: {str(e)}")
        raise

print("Merchant aggregation processing function defined")

# %% Cell 5
# Simple streaming query setup
def start_streaming_pipeline():
    """Start the simple streaming pipeline"""
    try:
        print("Starting simple streaming pipeline...")
        
        # Read streaming data from raw table using CDC
        streaming_df = spark.readStream \
            .format("delta") \
            .option("readChangeFeed", "true") \
            .option("startingVersion", "latest") \
            .table(raw_table)
        
        # Process each batch
        def process_batch(batch_df, batch_id):
            print(f"Processing batch {batch_id}")
            process_merchant_aggregations(batch_df, batch_id)
            print(f"Batch {batch_id} processed successfully.")
        
        # Start streaming query
        query = streaming_df.writeStream \
            .foreachBatch(process_batch) \
            .trigger(processingTime='30 seconds') \
            .option("checkpointLocation", f"/tmp/checkpoint_test_{catalog_name}_{schema_name}_merchant_agg") \
            .start()
        
        print("Streaming pipeline started successfully!")
        return query
        
    except Exception as e:
        print(f"Error starting streaming pipeline: {str(e)}")
        raise

print("Streaming pipeline function defined")

# %% Cell 6
# Start the streaming pipeline
print("Starting simple streaming pipeline...")
streaming_query = start_streaming_pipeline()
print("Streaming pipeline is running!")
