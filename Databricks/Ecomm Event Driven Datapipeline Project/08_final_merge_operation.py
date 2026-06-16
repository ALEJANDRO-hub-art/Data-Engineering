# Converted from: 08_final_merge_operation(2).ipynb
# Source: Jupyter Notebook

# %% [markdown] Cell 1
# # Final Merge Operation and Data Consolidation
# This notebook performs the final merge operation to consolidate all processed data into target tables with SCD2 (Slowly Changing Dimension) logic.

# %% [code] Cell 2
# Configuration
from delta.tables import *

# Source tables
enriched_orders_table = "`demo-external-catalog`.default.enriched_orders"
customer_analytics_table = "`demo-external-catalog`.default.customer_analytics"
product_analytics_table = "`demo-external-catalog`.default.product_analytics"

# Target tables
orders_target = "`demo-external-catalog`.default.orders_target"
customers_target = "`demo-external-catalog`.default.customers_target"
products_target = "`demo-external-catalog`.default.products_target"
inventory_target = "`demo-external-catalog`.default.inventory_target"
shipping_target = "`demo-external-catalog`.default.shipping_target"
analytics_summary_table = "`demo-external-catalog`.default.analytics_summary"

print("Starting final merge operation...")

# %% [code] Cell 3
# Import required libraries
from pyspark.sql import functions as F
from pyspark.sql.types import *
from datetime import datetime
import json

# Read enriched data
try:
    df_enriched_orders = spark.read.table(enriched_orders_table)
    df_customer_analytics = spark.read.table(customer_analytics_table)
    df_product_analytics = spark.read.table(product_analytics_table)
    
    print("Successfully loaded enriched datasets")
    print(f"Enriched orders: {df_enriched_orders.count()} records")
    print(f"Customer analytics: {df_customer_analytics.count()} records")
    print(f"Product analytics: {df_product_analytics.count()} records")
    
except Exception as e:
    print(f"Error loading enriched datasets: {str(e)}")
    raise

# %% [code] Cell 4
# Merge Orders Data with SCD2 Logic
try:
    # Prepare orders data for merge
    df_orders_merge = df_enriched_orders.select(
        "order_id", "customer_id", "product_id", "order_date", "order_amount",
        "currency", "payment_method", "shipping_address", "order_status",
        "created_timestamp", "processed_timestamp", "batch_id", "source_system",
        "order_profit_margin", "estimated_clv", "season", "day_of_week",
        "is_weekend", "time_of_day"
    ).withColumn("effective_date", F.current_date()) \
     .withColumn("expiry_date", F.lit(None).cast(DateType())) \
     .withColumn("is_current", F.lit(True))
    
    # Check if target table exists
    if spark.catalog.tableExists(orders_target):
        # Perform SCD2 merge
        target_orders = DeltaTable.forName(spark, orders_target)
        
        # Set expiry date for existing records that will be updated
        target_orders.update(
            condition=F.col("order_id").isin([row.order_id for row in df_orders_merge.select("order_id").distinct().collect()]),
            set={
                "expiry_date": F.current_date(),
                "is_current": F.lit(False)
            }
        )
        
        # Insert new records
        df_orders_merge.write.format("delta").mode("append").saveAsTable(orders_target)
        
    else:
        # Create new table
        df_orders_merge.write.format("delta").saveAsTable(orders_target)
    
    print("Orders merge completed successfully")
    
except Exception as e:
    print(f"Error merging orders data: {str(e)}")
    raise

# %% [code] Cell 5
# Merge Customers Data with SCD2 Logic

try:
    df_customers_merge = df_customer_analytics.select(
        "customer_id", "first_name", "last_name", "email", "phone",
        "date_of_birth", "registration_date", "address", "city", "state",
        "zip_code", "country", "customer_tier", "last_login", "customer_created_timestamp",
        "age", "age_segment", "days_since_registration", "lifecycle_stage",
        "total_orders", "total_spent", "avg_order_value", "customer_segment"
    ).withColumn("effective_date", F.current_date()) \
     .withColumn("expiry_date", F.lit(None).cast(DateType())) \
     .withColumn("is_current", F.lit(True))
    
    if spark.catalog.tableExists(customers_target):
        target_customers = DeltaTable.forName(spark, customers_target)
        target_customers.update(
            condition=F.col("customer_id").isin([row.customer_id for row in df_customers_merge.select("customer_id").distinct().collect()]),
            set={
                "expiry_date": F.current_date(),
                "is_current": F.lit(False)
            }
        )
        df_customers_merge.write.format("delta").mode("append").saveAsTable(customers_target)
    else:
        df_customers_merge.write.format("delta").saveAsTable(customers_target)
    print("Customers merge completed successfully")
except Exception as e:
    print(f"Error merging customers data: {str(e)}")
    raise

# %% [code] Cell 6
# Merge Products Data with SCD2 Logic
try:
    # Prepare products data for merge
    df_products_merge = df_product_analytics.select(
        "product_id", "product_name", "category", "subcategory", "brand",
        "price", "product_currency", "product_stock_quantity", "product_weight_kg", "dimensions_cm",
        "color", "material", "description", "launch_date", "discontinued",
        "product_created_timestamp", "product_price_segment", "product_stock_status", "days_since_launch",
        "product_lifecycle_stage", "volume_cm3", "density_kg_per_cm3", "total_orders",
        "total_revenue", "unique_customers", "performance_category", "product_lifecycle"
    ).withColumn("effective_date", F.current_date()) \
     .withColumn("expiry_date", F.lit(None).cast(DateType())) \
     .withColumn("is_current", F.lit(True))
    
    # Check if target table exists
    if spark.catalog.tableExists(products_target):
        # Perform SCD2 merge
        target_products = DeltaTable.forName(spark, products_target)
        
        # Set expiry date for existing records that will be updated
        target_products.update(
            condition=F.col("product_id").isin([row.product_id for row in df_products_merge.select("product_id").distinct().collect()]),
            set={
                "expiry_date": F.current_date(),
                "is_current": F.lit(False)
            }
        )
        
        # Insert new records
        df_products_merge.write.format("delta").mode("append").saveAsTable(products_target)
        
    else:
        # Create new table
        df_products_merge.write.format("delta").saveAsTable(products_target)
    
    print("Products merge completed successfully")
    
except Exception as e:
    print(f"Error merging products data: {str(e)}")
    raise

# %% [code] Cell 7
# Create Analytics Summary Dashboard
try:
    # Create comprehensive analytics summary
    analytics_summary = df_enriched_orders.agg(
        F.count("order_id").alias("total_orders"),
        F.sum("order_amount").alias("total_revenue"),
        F.avg("order_amount").alias("avg_order_value"),
        F.countDistinct("customer_id").alias("unique_customers"),
        F.countDistinct("product_id").alias("unique_products"),
        F.sum("order_profit_margin").alias("total_profit"),
        F.avg("estimated_clv").alias("avg_estimated_clv")
    ).withColumn("profit_margin_percentage", F.col("total_profit") / F.col("total_revenue") * 100) \
     .withColumn("revenue_per_customer", F.col("total_revenue") / F.col("unique_customers")) \
     .withColumn("orders_per_customer", F.col("total_orders") / F.col("unique_customers")) \
     .withColumn("report_date", F.current_date()) \
     .withColumn("report_timestamp", F.current_timestamp())
    
    # Add seasonal analysis
    seasonal_analysis = df_enriched_orders.groupBy("season") \
        .agg(
            F.count("order_id").alias("orders_count"),
            F.sum("order_amount").alias("seasonal_revenue"),
            F.avg("order_amount").alias("avg_seasonal_order_value")
        )
    
    # Add customer segment analysis
    segment_analysis = df_customer_analytics.groupBy("customer_segment") \
        .agg(
            F.count("customer_id").alias("customers_count"),
            F.sum("total_spent").alias("segment_revenue"),
            F.avg("total_spent").alias("avg_segment_value")
        )
    
    # Add product category analysis
    category_analysis = df_product_analytics.groupBy("category") \
        .agg(
            F.count("product_id").alias("products_count"),
            F.sum("total_revenue").alias("category_revenue"),
            F.avg("total_revenue").alias("avg_category_revenue")
        )
    
    print("Analytics summary created successfully")
    
except Exception as e:
    print(f"Error creating analytics summary: {str(e)}")
    raise

# %% [code] Cell 8
# Write Analytics Summary to Table
try:
    # Write main analytics summary
    analytics_summary.write.format("delta").mode("overwrite").saveAsTable(analytics_summary_table)
    
    # Write seasonal analysis
    seasonal_analysis.write.format("delta").mode("overwrite").saveAsTable("`demo-external-catalog`.default.seasonal_analysis")
    
    # Write segment analysis
    segment_analysis.write.format("delta").mode("overwrite").saveAsTable("`demo-external-catalog`.default.segment_analysis")
    
    # Write category analysis
    category_analysis.write.format("delta").mode("overwrite").saveAsTable("`demo-external-catalog`.default.category_analysis")
    
    print("Analytics summary tables created successfully")
    
    # Get final statistics
    final_stats = analytics_summary.collect()[0]
    
    print("Final Analytics Summary:")
    print(f"Total Orders: {final_stats['total_orders']}")
    print(f"Total Revenue: ${final_stats['total_revenue']:,.2f}")
    print(f"Average Order Value: ${final_stats['avg_order_value']:,.2f}")
    print(f"Unique Customers: {final_stats['unique_customers']}")
    print(f"Unique Products: {final_stats['unique_products']}")
    print(f"Total Profit: ${final_stats['total_profit']:,.2f}")
    print(f"Profit Margin: {final_stats['profit_margin_percentage']:.2f}%")
    print(f"Revenue per Customer: ${final_stats['revenue_per_customer']:,.2f}")
    print(f"Orders per Customer: {final_stats['orders_per_customer']:.2f}")
    
except Exception as e:
    print(f"Error writing analytics summary: {str(e)}")
    raise

# %% [code] Cell 9
from pyspark.sql.types import StructType, StructField, LongType, StringType

merge_summary = {
    "archived_files": None,
    "invalid_records": None,
    "status": "SUCCESS",
    "task": "final_merge_operation",
    "timestamp": datetime.now().isoformat(),
    "total_records": int(final_stats['total_orders']),
    "valid_records": int(final_stats['total_orders'])
}

print("Final Merge Summary:")
print(json.dumps(merge_summary, indent=2))

processing_log_schema = StructType([
    StructField("archived_files", LongType(), True),
    StructField("invalid_records", LongType(), True),
    StructField("status", StringType(), True),
    StructField("task", StringType(), True),
    StructField("timestamp", StringType(), True),
    StructField("total_records", LongType(), True),
    StructField("valid_records", LongType(), True)
])

summary_df = spark.createDataFrame([merge_summary], schema=processing_log_schema)
summary_df.write.format("delta").mode("append").saveAsTable("`demo-external-catalog`.default.processing_log")

dbutils.jobs.taskValues.set("final_merge_status", "SUCCESS")
dbutils.jobs.taskValues.set("total_revenue", float(final_stats['total_revenue']))
dbutils.jobs.taskValues.set("total_orders", int(final_stats['total_orders']))

print("Event-driven pipeline processing completed successfully!")
