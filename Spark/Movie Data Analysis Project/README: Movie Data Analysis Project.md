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








