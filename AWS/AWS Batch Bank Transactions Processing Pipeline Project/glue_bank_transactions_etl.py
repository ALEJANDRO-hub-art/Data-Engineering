import sys
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

args = getResolvedOptions(
    sys.argv,
    ["JOB_NAME", "SOURCE_BUCKET", "SOURCE_KEY", "TARGET_PATH"]
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

source_bucket = args["SOURCE_BUCKET"]
source_key = args["SOURCE_KEY"]
target_path = args["TARGET_PATH"]

input_path = f"s3://{source_bucket}/{source_key}"

# Read JSON file
df = spark.read.option("multiline", "true").json(input_path)

# Count source rows
source_count = df.count()

# Data quality checks
df_clean = df.filter(
    F.col("transaction_id").isNotNull() &
    F.col("transaction_date").isNotNull() &
    F.col("amount").isNotNull()
)

# Deduplicate based on transaction_id
df_dedup = df_clean.dropDuplicates(["transaction_id"])

processed_count = df_dedup.count()

# Add partition column
df_final = df_dedup.withColumn("processing_date", F.current_date())

# Write Parquet
df_final.write.mode("append").partitionBy("processing_date").parquet(target_path)

# Print logs for CloudWatch
print(f"Input file: {input_path}")
print(f"Source count: {source_count}")
print(f"Processed count: {processed_count}")
print(f"Rejected count: {source_count - processed_count}")

job.commit()
