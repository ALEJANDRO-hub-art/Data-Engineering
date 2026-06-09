I have this Marketing Campaign Data Analysis Using PySpark Project.

<img width="687" height="260" alt="image" src="https://github.com/user-attachments/assets/d6428b6b-3f6e-431d-8995-7d849467b6ee" />

This is a PySpark + HDFS + Hive project for marketing campaign analytics.

**1. What each file does**

**HQL_DataStore.txt**
- Contains the Hive SQL commands to create external Hive tables for Q1, Q2, and Q3 outputs using JSON SerDe.

**Spark Assignment 1.pdf**
- This is the assignment document. It explains the required input files: ad_campaigns_data.json, user_profile_data.json, and store_data.json, plus the 3 questions you must solve using PySpark.

**Spark_Marketingdata.py**
- Python script version of the PySpark solution. It reads JSON files from HDFS, creates Spark DataFrames, solves Q1/Q2/Q3, and writes output back to HDFS.

**2. Missing files you need**

The project needs these 3 JSON files:

- ad_campaigns_data.json
- user_profile_data.json
- store_data.json

They are the input data files described in the PDF assignment.

Download/create them inside your local project folder:

<img width="607" height="145" alt="image" src="https://github.com/user-attachments/assets/e72ae9a1-dced-430b-a5bb-96cbc55f6c93" />


Here are the JSON files inside the Project Folder.

<img width="662" height="307" alt="image" src="https://github.com/user-attachments/assets/cbef9e19-95a6-4b67-9116-6d011f2d7daf" />

<img width="644" height="261" alt="image" src="https://github.com/user-attachments/assets/bda71286-6301-4e8d-81ca-c13101cd8ff9" />

Open your Windows Command Prompt.

Do:

- cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 3\Spark_Assignment_Solution\Spark_Assignment_1_Solution"

<img width="653" height="290" alt="image" src="https://github.com/user-attachments/assets/aa3b5db8-cf3f-41fa-81a0-1a3396cf7319" />

The assignment expects HDFS + Spark + Hive together.

A single Docker container (or Docker Compose stack) can easily provide Hadoop, Spark, and Hive on one machine. 

The paths and commands shown in your earlier screenshots are consistent with a local pseudo-distributed Hadoop environment running inside containers.

Use Docker Compose. It is easier than one single container because HDFS, Spark, and Hive usually run as separate services.

HDFS + Spark + Hive with Docker Compose

**1. Create project folder**

In yout project folder:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 3\Spark_Assignment_Solution\Spark_Assignment_1_Solution

Put the **docker-compose.yml** inside the project folder. We are going to create this **docker-compose.yml** file.

Create **docker-compose.yml**

Create a file named: **docker-compose.yml**

**It looks like:**

-------------------------------------------------------------------------------------------------------------------------

```yaml
version: "3"

services:
  namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
    container_name: namenode
    ports:
      - "9870:9870"
      - "9000:9000"
    environment:
      - CLUSTER_NAME=test
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

  hive-server:
    image: bde2020/hive:2.3.2-postgresql-metastore
    container_name: hive-server
    depends_on:
      - namenode
      - datanode
    ports:
      - "10000:10000"
    environment:
      - HIVE_CORE_CONF_javax_jdo_option_ConnectionURL=jdbc:postgresql://hive-metastore/metastore
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000

  hive-metastore:
    image: bde2020/hive:2.3.2-postgresql-metastore
    container_name: hive-metastore
    depends_on:
      - namenode
      - datanode
      - hive-metastore-postgresql
    command: /opt/hive/bin/hive --service metastore
    environment:
      - SERVICE_PRECONDITION=namenode:9870 datanode:9864 hive-metastore-postgresql:5432
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000

  hive-metastore-postgresql:
    image: bde2020/hive-metastore-postgresql:2.3.0
    container_name: hive-metastore-postgresql

  spark-master:
    image: bde2020/spark-master:3.3.0-hadoop3.3
    container_name: spark-master
    ports:
      - "8080:8080"
      - "7077:7077"
    environment:
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000
    volumes:
      - ./:/project

  spark-worker:
    image: bde2020/spark-worker:3.3.0-hadoop3.3
    container_name: spark-worker
    depends_on:
      - spark-master
    ports:
      - "8081:8081"
    environment:
      - SPARK_MASTER=spark://spark-master:7077
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000
    volumes:
      - ./:/project

volumes:
  hadoop_namenode:
  hadoop_datanode:
```

-------------------------------------------------------------------------------------------------------------------------

So we create this docker-compose.yml file and pasted in the project folder:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 3\Spark_Assignment_Solution\Spark_Assignment_1_Solution

<img width="660" height="330" alt="image" src="https://github.com/user-attachments/assets/51d1c38f-8df8-44c9-b3fe-7225b42250a6" />

**Open Docker Desktop GUI**

- Open Docker Desktop.
  - Wait until it says Docker Desktop is running.
- Go to Containers.
- Keep Docker Desktop open.















