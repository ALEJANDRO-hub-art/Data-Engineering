I have the following project Movie Data Analysis Project

<img width="679" height="375" alt="image" src="https://github.com/user-attachments/assets/d541b245-d333-4fb5-aa70-2812383b7f44" />

Your project is a Spark Movie Data Analysis project. The assignment requires **Hadoop/YARN/Hive/Spark**, **loading movies.csv**, **ratings.csv**, and **tags.csv** into HDFS, running a Spark job, and saving each result as a single CSV with headers in an HDFS output path.

**Files and where they go**

Put all project files in one local Windows folder first:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 3\Spark_Assignment_Solution\Spark_Assignment_2_Solution

Your files:

<img width="715" height="508" alt="image" src="https://github.com/user-attachments/assets/4657a3c8-fbe6-4c20-aedb-581555c91a92" />

<img width="698" height="411" alt="image" src="https://github.com/user-attachments/assets/4c925c60-c6a6-44f2-8005-6a8fe43496dc" />

Where to upload files

Inside HDFS, upload the files here:

- /tmp/spark_movie/

Expected HDFS files:

- /tmp/spark_movie/movies.csv
- /tmp/spark_movie/ratings.csv
- /tmp/spark_movie/tags.csv

Your Spark code already reads from these paths.

For your assignment, use Docker Compose.

- namenode  = HDFS master
- datanode  = HDFS storage
- spark     = runs PySpark job
- hive      = Hive metastore/query layer

In Windows File Explorer, create:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 3\Spark_Assignment_Solution\Spark_Assignment_2_Solution

Put these files inside:

- docker-compose.yml
- Spark_MovieRating.py
- movies.csv
- ratings.csv
- tags.csv

Your Python file is the Spark executable job

Lets build this **docker-compose.yml** file. We can find it in the Project Folder.

<img width="676" height="397" alt="image" src="https://github.com/user-attachments/assets/fc11b128-a5b1-41ac-ba0c-4482504bd851" />

Lets inspect this **docker-compose.yaml** file:

```yaml
version: "3.8"

services:
  namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
    container_name: namenode
    ports:
      - "9870:9870"
      - "9000:9000"
    environment:
      - CLUSTER_NAME=spark-hive-cluster
    volumes:
      - hadoop_namenode:/hadoop/dfs/name

  datanode:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8
    container_name: datanode
    depends_on:
      - namenode
    ports:
      - "9864:9864"
    environment:
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000
    volumes:
      - hadoop_datanode:/hadoop/dfs/data

  spark:
    image: bitnami/spark:3.5
    container_name: spark
    depends_on:
      - namenode
      - datanode
    ports:
      - "4040:4040"
    volumes:
      - ./:/app
    working_dir: /app
    command: sleep infinity

volumes:
  hadoop_namenode:
  hadoop_datanode:
```

Open the Windows Command Prompt (cmd).

cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 3\Spark_Assignment_Solution\Spark_Assignment_2_Solution"

**Start containers**

Run:

- docker compose up -d

Check containers:

- docker ps

You should see:

- namenode
- datanode
- spark

**Open Hadoop GUI**

Open browser:

- http://localhost:9870

This is the **HDFS NameNode GUI.**

Go to:

- Utilities → Browse the file system

**Copy files into Spark container**

Use your Spark container name. Example:

- docker cp movies.csv spark-master:/tmp/movies.csv
- docker cp ratings.csv spark-master:/tmp/ratings.csv
- docker cp tags.csv spark-master:/tmp/tags.csv
- docker cp Spark_MovieRating.py spark-master:/tmp/Spark_MovieRating.py

**Enter Spark container**
- docker exec -it spark-master bash

**Create HDFS folders**

Inside the container:

- hdfs dfs -mkdir -p /tmp/spark_movie
- hdfs dfs -mkdir -p /tmp/output_data/spark_movie

Upload CSV files to HDFS

- hdfs dfs -put -f /tmp/movies.csv /tmp/spark_movie/movies.csv
- hdfs dfs -put -f /tmp/ratings.csv /tmp/spark_movie/ratings.csv
- hdfs dfs -put -f /tmp/tags.csv /tmp/spark_movie/tags.csv

**Verify:**

- hdfs dfs -ls /tmp/spark_movie

You should see:

- movies.csv
- ratings.csv
- tags.csv

**Run the Spark job**

- spark-submit /tmp/Spark_MovieRating.py

The script creates Spark SQL temp views:

- MOVIES
- RATINGS
- TAGS

Then it runs the assignment queries and saves each output into HDFS.

Whats inside **Spark_MovieRating.py** file:

This script is a PySpark marketing analytics project that **reads three JSON datasets, joins them, aggregates marketing events, and saves the results as JSON output files.**

<img width="563" height="526" alt="image" src="https://github.com/user-attachments/assets/b560b43a-1f16-4f83-aecf-b2636c871b15" />

In one sentence: **the script calculates marketing event counts (impressions, clicks, video ads) by operating system, store, and gender using Spark, then saves the aggregated results as JSON files.**

**Expected output folders in HDFS**

Your script writes results here:

- /tmp/output_data/spark_movie/

Important outputs include:

- agg_Ratings.csv
- avg_monthly_Ratings.csv
- distribution_ratings.csv
- tagged_not_rated.csv
- rated_not_tagged.csv
- top_10_avgratings&count_ratings.csv
- tags_per_movieVStags_per_user.csv
- users_tagged_not_rate.csv
- ratings_per_userVSratings_per_movie.csv
- freq_genre_per_rating.csv
- freq_tag_per_genre.csv
- popular_movies.csv
- top_10_morethan30users.csv

The assignment **asks each problem result to be stored as a single CSV** with header in an HDFS output path.

Verify outputs:

- hdfs dfs -ls /tmp/output_data/spark_movie

View one output:

- hdfs dfs -cat /tmp/output_data/spark_movie/agg_Ratings.csv/part-*.csv

**GUI verification in browser**

Open your browser:

- http://localhost:9870

This is the **HDFS NameNode GUI.**

Then go to:

Utilities
- → Browse the file system
- → tmp
- → output_data
- → spark_movie

You should see the output folders created by Spark.

**Download output files from HDFS**

Inside the container:

- hdfs dfs -get -f /tmp/output_data/spark_movie /tmp/spark_movie_outputs

Then from Windows CMD:

- docker cp spark-master:/tmp/spark_movie_outputs "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 3\Spark_Assignment_Solution\Spark_Assignment_2_Solution\spark_movie_outputs"

Now your output CSV folders are in:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 3\Spark_Assignment_Solution\Spark_Assignment_2_Solution\spark_movie_outputs


















