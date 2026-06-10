I have the following project Orders-Customers Data Analysis Project:

<img width="657" height="214" alt="image" src="https://github.com/user-attachments/assets/588fee74-b98f-4428-ac00-e03c3d146a5a" />

<img width="642" height="210" alt="image" src="https://github.com/user-attachments/assets/982095d6-9763-48fe-a5c5-05720d2c0a30" />

Files and where they go, Your project folder should look like this:

<img width="677" height="179" alt="image" src="https://github.com/user-attachments/assets/7fca1455-6808-4267-acc6-b329a4629602" />

The CSV files are loaded into Hive tables from /tmp/input_data/. The HQL file creates the tables_by_spark database, creates orders/customers Hive tables, loads the CSVs, then creates Parquet tables orders_pq and customers_pq.

**You run this in a Docker Compose Spark + Hive + HDFS environment.**

I have created a docker-compose.yml file, look like:

```yaml
version: "3.8"

services:
  namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
    container_name: namenode
    hostname: namenode
    ports:
      - "9870:9870"
      - "9000:9000"
    environment:
      - CLUSTER_NAME=spark-hive-cluster
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000
    volumes:
      - hadoop_namenode:/hadoop/dfs/name

  datanode:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8
    container_name: datanode
    hostname: datanode
    depends_on:
      - namenode
    ports:
      - "9864:9864"
    environment:
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000
      - SERVICE_PRECONDITION=namenode:9870
    volumes:
      - hadoop_datanode:/hadoop/dfs/data

  hive-metastore-postgresql:
    image: bde2020/hive-metastore-postgresql:2.3.0
    container_name: hive-metastore-postgresql
    hostname: hive-metastore-postgresql

  hive-metastore:
    image: bde2020/hive:2.3.2-postgresql-metastore
    container_name: hive-metastore
    hostname: hive-metastore
    depends_on:
      - namenode
      - datanode
      - hive-metastore-postgresql
    environment:
      - HIVE_CORE_CONF_javax_jdo_option_ConnectionURL=jdbc:postgresql://hive-metastore-postgresql/metastore
      - SERVICE_PRECONDITION=namenode:9870 datanode:9864 hive-metastore-postgresql:5432
    command: /opt/hive/bin/hive --service metastore
    ports:
      - "9083:9083"

  hive-server:
    image: bde2020/hive:2.3.2-postgresql-metastore
    container_name: hive-server
    hostname: hive-server
    depends_on:
      - hive-metastore
    environment:
      - HIVE_CORE_CONF_javax_jdo_option_ConnectionURL=jdbc:postgresql://hive-metastore-postgresql/metastore
      - HIVE_SITE_CONF_hive_metastore_uris=thrift://hive-metastore:9083
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000
      - SERVICE_PRECONDITION=hive-metastore:9083
    ports:
      - "10000:10000"

  spark:
    image: bitnami/spark:3.5
    container_name: spark
    hostname: spark
    depends_on:
      - namenode
      - datanode
      - hive-server
    user: root
    working_dir: /app
    volumes:
      - ./:/app
    environment:
      - HADOOP_CONF_DIR=/opt/bitnami/spark/conf
      - SPARK_MODE=master
    ports:
      - "4040:4040"
      - "8080:8080"
    command: sleep infinity

volumes:
  hadoop_namenode:
  hadoop_datanode:
```

<img width="663" height="242" alt="image" src="https://github.com/user-attachments/assets/4d00ad01-2afe-4083-9e9f-47eff204c4a3" />

Open Docker Desktop.

Open your project folder: Code_Files. Click the address bar, type: cmd. This is the Windows Prompt (cmd).

Do:

cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 4\Code_Files"

Run:
- docker compose up -d

In Docker Desktop, go to Containers and confirm these are running:
- namenode
- datanode
- hive-metastore
- hive-server
- spark

Then check:
- docker ps

You should see Spark, Hive, and Hadoop containers running.

**Copy CSV files into HDFS**

Enter the Spark container:
- docker exec -it spark bash

Create HDFS folder:
- hdfs dfs -mkdir -p /tmp/input_data

Copy files from your mounted project folder into HDFS:

- hdfs dfs -put -f /app/Dataset/customers_dataset.csv /tmp/input_data/
- hdfs dfs -put -f /app/Dataset/orders_dataset.csv /tmp/input_data/

Check:
- hdfs dfs -ls /tmp/input_data

You should see:
- customers_dataset.csv
- orders_dataset.csv

**Run Hive table commands**

Inside the Spark container, run:
- hive -f /app/Hive_Table_Commands.hql

This creates the Hive database/tables used by Spark.

**Run the Spark job**

Still inside the Spark container, run:
- spark-submit /app/Orders_Data_Analysis_App.py

The output is written to:
- /tmp/spark_output/final_result

**Docker Desktop GUI steps**

In **Docker Desktop:**

Open Docker Desktop

Go to **Containers**. Find your Compose project

Confirm these containers are running:
- namenode
- datanode
- hive-server
- spark

Click the **spark** container. Open the Terminal tab

Run:
- hdfs dfs -ls /tmp/input_data
- hive -f /app/Hive_Table_Commands.hql
- spark-submit /app/Orders_Data_Analysis_App.py

<img width="708" height="340" alt="image" src="https://github.com/user-attachments/assets/d6b8aa24-3a20-4185-aeaf-53c2f78654bc" />


















