# %%
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from datetime import datetime
from pyspark.sql.functions import from_unixtime

# Create Spark session
spark = SparkSession.builder \
    .appName("Spark with Hive") \
    .enableHiveSupport() \
    .getOrCreate()

# %%
# Reading movies data

hdfs_path = '/tmp/spark_movie/movies.csv'
df_movies = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load(hdfs_path)

# Print schema and sample data
df_movies.printSchema()
df_movies.show(5)

# %%
# Define the correct schema based on your CSV structure
schema = StructType([
    StructField("userId", IntegerType(), True),
    StructField("movieId", IntegerType(), True),
    StructField("rating", FloatType(), True),
    StructField("timestamp",IntegerType(), True),
])
hdfs_path = '/tmp/spark_movie/ratings.csv'
# Read the CSV file into a DataFrame
df_ratings = spark.read.format('csv').option('header', 'true').option('inferSchema', 'false').schema(schema).load(hdfs_path)

# Convert timestamp to TimestampType
df_ratings = df_ratings.withColumn("timestamp", from_unixtime("timestamp").cast(TimestampType()))

# Show the DataFrame
df_ratings.show()

# %%
# Define the correct schema based on your CSV structure
schema = StructType([
    StructField("userId", IntegerType(), True),
    StructField("movieId", IntegerType(), True),
    StructField("tag", StringType(), True),
    StructField("timestamp",IntegerType(), True),
])

hdfs_path = '/tmp/spark_movie/tags.csv'
# Read the CSV file into a DataFrame
df_tags = spark.read.format('csv').option('header', 'true').option('inferSchema', 'false').schema(schema).load(hdfs_path)

# Convert timestamp to TimestampType
df_tags = df_tags.withColumn("timestamp", from_unixtime("timestamp").cast(TimestampType()))

# Show the DataFrame
df_tags.show()

# %%
# Work with spark SQL

df_movies.createOrReplaceTempView("MOVIES")
df_ratings.createOrReplaceTempView("RATINGS")
df_tags.createOrReplaceTempView("TAGS")

# %%
# Aggregated number of ratings per year

query= """Select year(timestamp) as year,count(rating) as ratings 
       from RATINGS 
       group by 1 
        order by year(timestamp) desc"""


output = spark.sql(query)
output.show()

# Write data in HDFS into single file

# output.coalesce(1).write.format('csv').option('header', 'true').option('delimiter', ',').save('/tmp/output_data/spark_movie/')
output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/agg_Ratings.csv')
print("Write Successfull")

# %%
# Average Monthly number of ratings

query= """Select left(timestamp,7) as year_month,avg(rating) as avg_rating
       from RATINGS 
       group by 1 
        order by  left(timestamp,7) desc"""


output = spark.sql(query)
output.show()

# Write data in HDFS into single file

# output.coalesce(1).write.format('csv').option('header', 'true').option('delimiter', ',').save('/tmp/output_data/spark_movie/')
output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/avg_monthly_Ratings.csv')
print("Write Successfull")

# %%
# Ratings Level Distribution

query= """with t1 as (
    Select rating,case when rating between 0 and 2 THEN '0.0-2.0'
    WHEN rating between 2.3 and 4 THEN '2.5-4.0'
    ELSE '>4' END as rating_bucket
    from RATINGS),
    
    t2 as (select rating_bucket,count(rating) as counts
    from t1
    group by 1
    order by 1)
    
    Select rating_bucket,counts,counts*100/sum(counts)over() as percentage
    from t2"""

# Select rating_bucket,count(*) as counts
# from t1
# group by 1
# order by 1"""


output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/distribution_ratings.csv')
print("Write Successfull")

# %%
# Movies Tagged but not Rated

query= """
          with t1 as (Select distinct 
          t.movieID from TAGS as t
          left join RATINGS as r
          on t.movieID=r.movieID
          where r.movieID IS NULL)
          
          Select m.title 
          from MOVIES as m
          inner join t1
          on m.movieID=t1.movieID
          order by 1"""
          

output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/tagged_not_rated.csv')
print("Write Successfull")

# %%
# Movies Rated but not Tagged

query= """
          with t1 as (Select distinct 
          r.movieID from RATINGS as r
          left join TAGS as t
          on t.movieID=r.movieID
          where t.movieID IS NULL)
          
          Select m.title 
          from MOVIES as m
          inner join t1
          on m.movieID=t1.movieID
          order by 1"""
          

output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/rated_not_tagged.csv')
print("Write Successfull")

# %%
# Rated but untagged movies (With more than 30 user ratings) -- Top Movies in terms of avg rating and number of ratings

query= """ with t1 as 
            (Select movieid
                from ratings
                 group by 1
              having count(distinct userid)>30),

        t2 as (Select 
           t1.movieID from t1
           left join TAGS as t
           on t1.movieID=t.movieID
           where t.movieID IS NULL),
          
           t3 as (Select m.title,m.movieID 
           from MOVIES as m
          inner join t2
           on m.movieID=t2.movieID
           order by 1),
           
           t4 as (Select t3.title,avg(r.rating) as avg_rating,
           dense_rank()over(order by avg(r.rating) desc) as avg_rank
           from t3 left join RATINGS as r
           on t3.movieID=r.movieID
           group by 1),
           
           t5 as (Select t3.title,count(rating) as counts,
           dense_rank()over(order by count(rating) desc) as count_rank
           from t3 left join RATINGS as r
           on t3.movieID=r.movieID
           group by 1)
           
           Select t4.title as Movie_title1,t4.avg_rank,Round(t4.avg_rating,4) as avg_rating,t5.title as Movie_title2,t5.count_rank,t5.counts
           from t4 inner join t5
           on t4.avg_rank=t5.count_rank
           where t4.avg_rank<=10 and t5.count_rank<=10
        
           """
          

output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/top_10_avgratings&count_ratings.csv')
print("Write Successfull")

# %%
# Tags per movie vs Tags per User

query= """with t1 as(
          Select '1' as key, round((sum(CASE when tag IS NOT NULL THEN 1 ELSE 0 END)/count(distinct movieid)),2) as tags_per_movie
          from TAGS),
          
          t2 as ( Select '1' as key, (sum(CASE WHEN tag IS NOT NULL THEN 1 ELSE 0 END)/count(distinct userid)) as tags_per_user
          from TAGS)
          
          Select t1.tags_per_movie,t2.tags_per_user,
          CASE WHEN tags_per_user>tags_per_movie THEN 'tags_per_user is higher'
          ELSE 'tags_per_movie is higher' END as Comparison
          from t1 inner join t2 on t1.key=t2.key"""
          

output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/tags_per_movieVStags_per_user.csv')
print("Write Successfull")

# %%
# Users that tagged but did not Rate movies

query= """
         
         Select distinct t.userid
         from TAGS as t
         left join RATINGS as r
         on t.movieID=r.movieID
         where r.userID is NULL"""
          

output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/users_tagged_not_rate.csv')
print("Write Successfull")

# %%
# Ratings per user versus Ratings per Movie

query= """with t1 as(
          Select '1' as key, round((SUM(CASE when rating IS NOT NULL THEN 1 ELSE 0 END)/count(distinct userid)),2) as ratings_per_user
          from RATINGS),
          
          t2 as ( Select '1' as key, round((sum(CASE WHEN rating IS NOT NULL THEN 1 ELSE 0 END)/count(distinct movieid)),2) as ratings_per_movie
          from RATINGS)
          
          Select t1.ratings_per_user,t2.ratings_per_movie
          from t1 inner join t2 on t1.key=t2.key"""


output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/ratings_per_userVSratings_per_movie.csv')
print("Write Successfull")

# %%
# Predominant Genre per rating level

query= """with t1 as(
          Select r.rating,m.genres,count(*) as counts,
          dense_rank()over(partition by r.rating order by count(*) desc) as ranker
          from RATINGS AS r
          left join MOVIES as m
          on r.movieID=m.movieID
          group by 1,2)
          
          Select rating,genres as most_frequent_genre from t1 
          where ranker=1
          order by rating desc"""


          

output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/freq_genre_per_rating.csv')
print("Write Successfull")

# %%
# Predominant tag per genre

query= """with t1 as(
          Select m.genres,t.tag,count(*) as counts,
          dense_rank()over(partition by m.genres order by count(*) desc) as ranker
          from MOVIES AS m
          left join TAGS as t
          on t.movieID=m.movieID
          group by 1,2)
          
          Select genres,tag as most_frequent_tag from t1 
          where ranker=1
          order by genres desc"""


          

output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/freq_tag_per_genre.csv')
print("Write Successfull")

# %%
# Top 10 popular movies (most users seen/rated it)

query= """with t1 as(
          Select r.movieID,m.title,count(distinct r.userID) as counts,
          dense_rank()over(order by count(distinct r.userid) desc) as ranker
          from RATINGS as r
          left join MOVIES as m
          on r.movieID=m.movieID
          group by 1,2)
          
          Select title,counts from t1 
          where ranker<=10
          """


          

output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/popular_movies.csv')
print("Write Successfull")

# %%
# Top 10 movies in terms of avg rating (>30 users reviewed)

query= """with t1 as(
          Select movieid,avg(rating) as avg_rating,
          dense_rank()over (order by avg(rating) desc) as ranker
          from RATINGS
          group by 1
          having count(distinct userID)>30)
          
          Select m.title,round(t1.avg_rating,9) as avg_rating,t1.ranker from t1
          left join MOVIES as m
          on t1.movieID=m.movieID
          where ranker<=10
          """


          

output = spark.sql(query)
output.show()

# Write data in HDFS into single file

output.coalesce(1).write.mode("overwrite").format('csv').option('header', 'true') .option('delimiter', ',').save('/tmp/output_data/spark_movie/top_10_morethan30users.csv')
print("Write Successfull")
