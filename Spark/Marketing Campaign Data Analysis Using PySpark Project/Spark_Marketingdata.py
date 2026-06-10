# %%
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, ArrayType

# Create Spark session
spark = SparkSession.builder \
    .appName("Spark with Hive") \
    .enableHiveSupport() \
    .getOrCreate()

# # Load the JSON data
hdfs_path1 = '/tmp/marketing_data/ad_campaigns_data.json'
hdfs_path2 = '/tmp/marketing_data/user_profile_data.json'
hdfs_path3 = '/tmp/marketing_data/store_data.json'


# Define the schema
schema_campaigns = StructType([
    StructField("campaign_id", StringType(), True),
    StructField("campaign_name", StringType(), True),
    StructField("campaign_country", StringType(), True),
    StructField("os_type", StringType(), True),
    StructField("device_type", StringType(), True),
    StructField("place_id", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("event_type", StringType(), True),
    StructField("event_time", TimestampType(), True)
])


schema_users = StructType([
    StructField("user_id", StringType(), True),
    StructField("country", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("age_group", StringType(), True),
    StructField("category", ArrayType(StringType()), True)
])


schema_stores = StructType([
    StructField("store_name", StringType(), True),
    StructField("place_ids", ArrayType(StringType()), True)
])


df_campaigns = spark.read.format('json').option("multiline", "true").schema(schema_campaigns).load(hdfs_path1)
df_users = spark.read.format('json').option("multiline", "true").schema(schema_users).load(hdfs_path2)
df_stores = spark.read.format('json').option("multiline", "true").schema(schema_stores).load(hdfs_path3)






# %%
# Print schema and sample data
df_campaigns.printSchema()
df_users.printSchema()
df_stores.printSchema()

# %%
# Show the dataframes
df_campaigns.show(5)
df_users.show(5)
df_stores.show(5)

# %%
# Extract date and hour from the event_time column
df_campaigns = df_campaigns.withColumn("event_time", F.col("event_time").cast("timestamp"))
df_campaigns = df_campaigns.withColumn("date", F.to_date("event_time"))
df_campaigns = df_campaigns.withColumn("hour", F.hour("event_time"))

# %%
# Define the output path
hdfs_output_path1 = '/tmp/marketing_data/output/'

# Q1. Analyze data for each campaign_id, date, hour, os_type & value to get all the events with counts
result_q1 = (
    df_campaigns.groupBy("campaign_id", "date", "hour", "os_type", "event_type")
    .agg(F.count("event_type").alias("event_count"))
    .groupBy("campaign_id", "date", "hour", "os_type")
    .pivot("event_type")
    .agg(F.first("event_count"))
    .fillna(0)
    .select(
        "campaign_id",
        "date",
        "hour",
        "os_type",
        F.struct(
            F.col("impression").alias("impression"),
            F.col("click").alias("click"),
            F.col("video ad").alias("video_ad"),
        ).alias("event"),
    )
)



# %%
result_q1.show()

# %%
# Save the result to HDFS
result_q1.write.json(hdfs_output_path1 + "q1_output", mode="overwrite")

# %%
# Define the output path
hdfs_output_path2 = '/tmp/marketing_data/output2/'

# Q2. Analyze data for each campaign_id, date, hour, store_name & value to get all the events with counts
result_q2 = (
    df_campaigns.join(df_stores, F.array_contains(df_stores.place_ids, df_campaigns.place_id), "inner")
    .groupBy("campaign_id", "date", "hour", "store_name", "event_type")
    .agg(F.count("event_type").alias("event_count"))
    .groupBy("campaign_id", "date", "hour", "store_name")
    .pivot("event_type")
    .agg(F.first("event_count"))
    .fillna(0)
    .select(
        "campaign_id",
        "date",
        "hour",
        "store_name",
        F.struct(
            F.col("impression").alias("impression"),
            F.col("click").alias("click"),
            F.col("video ad").alias("video_ad"),
        ).alias("event"),
    )
)

# %%
result_q2.show()

# %%
# Save the result to HDFS
result_q2.write.json(hdfs_output_path2 + "q2_output", mode="overwrite")

# %%
# Define the output path
hdfs_output_path3 = '/tmp/marketing_data/output3/'

# Q3. Analyze data for each campaign_id, date, hour, gender_type & value to get all the events with counts
result_q3 = (
    df_campaigns.join(df_users, "user_id", "inner")
    .groupBy("campaign_id", "date", "hour", "gender", "event_type")
    .agg(F.count("event_type").alias("event_count"))
    .groupBy("campaign_id", "date", "hour", "gender")
    .pivot("event_type")
    .agg(F.first("event_count"))
    .fillna(0)
    .select(
        "campaign_id",
        "date",
        "hour",
        "gender",
        F.struct(
            F.col("impression").alias("impression"),
            F.col("click").alias("click"),
            F.col("video ad").alias("video_ad"),
        ).alias("event"),
    )
)

# %%
result_q3.show()

# %%
# Save the result to HDFS
result_q3.write.json(hdfs_output_path3 + "q3_output", mode="overwrite")

# %%


