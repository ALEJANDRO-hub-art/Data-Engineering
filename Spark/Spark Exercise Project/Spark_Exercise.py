# %%
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from datetime import datetime

# Create Spark session
spark = SparkSession.builder \
    .appName("Spark with Hive") \
    .enableHiveSupport() \
    .getOrCreate()

data = [
    ["Product A", 1001, datetime.strptime("2023-07-20", "%Y-%m-%d"), datetime.strptime("2023-07-20 10:15:30", "%Y-%m-%d %H:%M:%S"), 29.99],
    ["Product B", 1002, datetime.strptime("2023-07-19", "%Y-%m-%d"), datetime.strptime("2023-07-19 14:20:45", "%Y-%m-%d %H:%M:%S"), 49.99],
    ["Product C", 1003, datetime.strptime("2023-07-18", "%Y-%m-%d"), datetime.strptime("2023-07-18 09:30:15", "%Y-%m-%d %H:%M:%S"), 39.99],
    ["Product D", 1004, datetime.strptime("2023-07-17", "%Y-%m-%d"), datetime.strptime("2023-07-17 16:45:00", "%Y-%m-%d %H:%M:%S"), 19.99]
]

# Define schema
schema = StructType([
    StructField("Product", StringType(), True),
    StructField("ID", IntegerType(), True),
    StructField("Date", DateType(), True),
    StructField("Timestamp", TimestampType(), True),
    StructField("Price", FloatType(), True)
])

df = spark.createDataFrame(data, schema)

df.printSchema()

df.show()

# %%
# First read example should not infer schema, ignore header row, provide explicit column name and datatype

# Define schema
schema = StructType([
    StructField("OrderID", StringType(), True),
    StructField("OrderItemID", IntegerType(), True),
    StructField("ProductID", StringType(), True),
    StructField("SellerID", StringType(), True),
    StructField("ShippingLimitDate", TimestampType(), True),
    StructField("Price", DoubleType(), True),
    StructField("FreightValue", DoubleType(), True)
])

hdfs_path = '/tmp/spark_datasets/order_items_dataset.csv'

df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'false').schema(schema).load(hdfs_path)

df.printSchema()

df.show(5)

# %%

# Second read example should infer schema, ignore header row

hdfs_path = '/tmp/spark_datasets/order_items_dataset.csv'

# File path pattern if we are reading from different hadoop cluster
# hdfs_path = 'hdfs://<namenode_host_ip_address>:<port>/tmp/spark_datasets/order_items_dataset.csv'

df = spark.read.format('csv').option('header','true').option('inferSchema','true').load(hdfs_path)

df.printSchema()

df.show()

# %%
# check default number of partitions
print(spark.sparkContext.defaultParallelism)

# %%
# check default size of each partition
print(spark.conf.get("spark.sql.files.maxPartitionBytes"))

# %%
print(f'Number of partitions: {df.rdd.getNumPartitions()}')

df_new = df.repartition(5)

print(f'Number of partitions: {df_new.rdd.getNumPartitions()}')

# %%
# Select columns in different options

from pyspark.sql.functions import *

df.select('order_id').show(5)

df.select('order_id', 'shipping_limit_date').show(5)

df.select(col('order_id'), col('shipping_limit_date')).show(5)

df.select(col('order_id').alias('oid'), col('shipping_limit_date').alias('limit_date')).show(5)

# %%
# Derive new column using withColumn

df2 = df.withColumn("year", year(col("shipping_limit_date"))).withColumn("month", month(col("shipping_limit_date")))

df2.select("order_id", "shipping_limit_date", "year", "month").show(5)

# %%
# Rename existing column using withColumnRenamed

df3 = df2.withColumnRenamed('shipping_limit_date', 'shipping_limit_datetime')

df3.select("order_id", "shipping_limit_datetime").show(5)

# %%
# Filter condition

df3.filter( col('order_id') == '00010242fe8c5a6d1ba2dd792cb16214' ).show(5)

order_ids = ['00010242fe8c5a6d1ba2dd792cb16214','00018f77f2f0320c557190d7a144bdd3']

df3.filter( col('order_id').isin(order_ids) ).show(5)

df3.filter( (col('price') < 50) & (col("freight_value")  < 10) ).show(5)

# SQL Type Expression
df3.filter("price < 50 and freight_value  < 10").show(5)

# %%
# Example to drop a column

df3.drop('month').show(5)

# %%
#drop duplicates row based on multiple columns

df3.dropDuplicates(['order_id', 'order_item_id']).show(5)

# order_id , order_item_id, c1, c2
#   1      ,    2        , A , B
#   1      ,    2        , A , B
#   1      ,    2        , C , D
#   1      ,    3        , E , F

# order_id , order_item_id, c1, c2
#   1      ,    2        , A , B
#   1      ,    3        , E , F

# %%
# get distinct rows

df3.dropDuplicates().show(5)

# %%
# arrange data using order by

df3.orderBy( col('price').desc() ).show(5)

df3.orderBy( col('price').asc(), col('freight_value').desc() ).show(5)

# %%
# Group By Operation

# on single column
df3.groupBy('year').agg( count('*').alias('total_count'),
                         avg('price').alias('avg_price'),
                         sum('price').alias('sum_price'),
                         min('price').alias('min_price'),
                         max('price').alias('max_price')
                       ).show(5)

# on multiple column
df3.groupBy('year', 'month').agg( count('*').alias('total_count'),
                                 avg('price').alias('avg_price'),
                                 sum('price').alias('sum_price'),
                                 min('price').alias('min_price'),
                                 max('price').alias('max_price')
                               ).orderBy( col('year').asc(), col('month').asc() ).show(20)

# %%
accum=spark.sparkContext.accumulator(0)

df3.foreach( lambda row: accum.add(row['price']) )

print(accum.value) #Accessed by driver

# %%
# Case-When statement

df3.withColumn("price_category", when( col('price') >= 100 , "High" )
                                .when( (col('price') < 100) & (col('price') >= 50) , "Medium" )
                                .otherwise("Low")).show(5)
                               

# %%
# Window functions

from pyspark.sql.window import Window

windowSpec1 = Window.partitionBy('year').orderBy( col('price').asc())

df3.withColumn("dense_rank" , dense_rank().over(windowSpec1) ).show(5)

windowSpec2 = Window.partitionBy('year').orderBy(col('shipping_limit_datetime').asc())

df3.withColumn('running_sum', sum('price').over(windowSpec2)).select('year','price','shipping_limit_datetime','running_sum').show(5)

# %%
hdfs_path = '/tmp/spark_datasets/sellers_dataset.csv'

sdf = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load(hdfs_path)

sdf.printSchema()
sdf.show(5)

# %%
# Join transformation

result1 = df3.join(broadcast(sdf), df3.seller_id == sdf.seller_id  , 'inner').drop(sdf.seller_id)

# df3.join(broadcast(sdf), df3.seller_id == sdf.seller_id  , 'inner').join(paydf, cond, 'left')

# result2 = result1.join(paydf, cond, 'left')

result1.printSchema()
result1.show(5)

# %%
# Perform join with alias names of dataframes

result2 = df3.alias('oid').join(sdf.alias('sid'), col('oid.seller_id') == col('sid.seller_id') , 'inner').drop(col('sid.seller_id'))


result2.printSchema()
result2.show(5)

# %%
# work with spark SQL

df3.createOrReplaceTempView("ORDER_ITEM")
sdf.createOrReplaceTempView("SELLERS")

joinedDF = spark.sql("select * from ORDER_ITEM oid INNER JOIN SELLERS sid ON oid.seller_id == sid.seller_id")

joinedDF.printSchema()

joinedDF.show(5)


# %%
# Write data in HDFS without any partition key

result1.write \
    .format('csv') \
    .mode('overwrite') \
    .option('header', 'true') \
    .option('delimiter', ',') \
    .save('/tmp/spark_output/result1')

print("Write Successfull")

# %%
# Write data in parquet format in HDFS without any partition key

result1.write \
    .format('parquet') \
    .mode('overwrite') \
    .save('/tmp/spark_output/result_pq')

print("Write Successfull")

# %%
# Write data in HDFS with partition key

result1.write.mode('overwrite').partitionBy('year').format('csv').option('header', 'true').option('delimiter', ',').save('/tmp/spark_output/result2')
print("Write Successfull")


# %%
# Write data in HDFS into single file

result1.coalesce(1).write.mode('overwrite').format('csv').option('header', 'true').option('delimiter', ',').save('/tmp/spark_output/result3/')

print("Write Successfull")

# %%
# Read json data in spark

file_path = '/tmp/spark_datasets/orders_json_data.json'

json_df = spark.read.json(file_path)

print("Original Schema :")
json_df.printSchema()

json_df.show(5)

# Explode the "purchases" array
purchases_df = json_df.select(
    "user_id",
    "name",
    "address",
    explode(col("purchases")).alias("purchase")
)

# Show the exploded schema
print("Exploded Schema:")
purchases_df.printSchema()
purchases_df.show(5)

# Further explode "items" within each purchase
items_df = purchases_df.select(
    "user_id",
    "name",
    "address",
    col("purchase.order_id").alias("order_id"),
    col("purchase.order_date").alias("order_date"),
    explode(col("purchase.items")).alias("item")
)

# Show the fully exploded DataFrame
print("Fully Exploded Data:")
items_df.show(truncate=False)

