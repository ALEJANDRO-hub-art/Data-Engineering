I have this Spark Exercise Project.

<img width="634" height="193" alt="image" src="https://github.com/user-attachments/assets/d73a3dde-471b-49f3-94d6-e31a55e15372" />

<img width="663" height="192" alt="image" src="https://github.com/user-attachments/assets/1876b7d8-ec59-4f88-af0b-f66f59f44e33" />

This is a PySpark practice/project exercise. It is not a full production app, but it demonstrates a Spark data processing workflow using CSV, JSON, joins, transformations, Spark SQL, partitions, and output writing.

Inside that same project folder, create:

<img width="430" height="132" alt="image" src="https://github.com/user-attachments/assets/db7e15c7-688b-42ff-a17b-b59bb672d715" />

The script expects these data files to exist in Spark/HDFS path:
- /tmp/spark_datasets/

So later you upload/copy the datasets there.

Brief explanation of what the script does

The script:
- Starts a SparkSession with Hive support
- Creates a small sample DataFrame manually
- Reads order_items_dataset.csv
- Demonstrates schema definition vs schema inference
- Selects, filters, renames, drops, sorts, and deduplicates columns
- Performs aggregations using groupBy
- Uses accumulators
- Uses case when logic
- Uses window functions like dense_rank and running sum
- Reads sellers_dataset.csv
- Joins order items with sellers
- Uses Spark SQL temporary views
- Writes output to CSV and Parquet
- Reads nested JSON and explodes arrays

**Step-by-step execution in GUI**

Open your Spark environment

Use one of these:
- Docker Desktop + Spark container
- Databricks Community Edition
- Local PySpark setup

Best option for your script: Docker/Spark or local PySpark, because the paths use:
- /tmp/spark_datasets/

**Use Docker Desktop + one Spark container.**

Dont you need a .yml file? No, There are two ways to run this project:

Option 1: Single Docker command (No .yml file needed)

This is what I described earlier:
- docker run -it --name spark_exercise -p 4040:4040 -v "%cd%":/app bitnami/spark:latest bash

This creates a temporary Spark container directly. For a simple exercise like yours, this is enough.

Option 2 — Docker Compose (docker-compose.yml)

This is better if:
- You do Spark projects frequently
- You want a reusable environment
- You want Hadoop + Spark + Hive later
- You want to start everything from Docker Desktop

We are using **Option 1.**

**Open the Windows Prompt (cmd).**

Do:

cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 3\Spark_Exercise"

**Start a Spark container**

Run:
- docker run -it --name spark_exercise -p 4040:4040 -v "%cd%":/app bitnami/spark:latest bash

This opens a terminal inside the Spark container. Now you are inside the container.

Your project folder is now available inside Docker at:
- /app

**Confirm files are visible inside Docker**

Run:
- ls /app
- ls /app/datasets

You should see:
- Spark_Exercise.py
- Spark_Exercise.ipynb
- datasets

And inside datasets:
- order_items_dataset.csv
- orders_json_data.json
- sellers_dataset.csv

**Create the folder expected by the script**

Run:
- mkdir -p /tmp/spark_datasets

**Copy dataset files**

Run:
- cp /app/datasets/order_items_dataset.csv /tmp/spark_datasets/
- cp /app/datasets/sellers_dataset.csv /tmp/spark_datasets/
- cp /app/datasets/orders_json_data.json /tmp/spark_datasets/

Check:
- ls /tmp/spark_datasets

**Run the PySpark project**

Run:
- spark-submit /app/Spark_Exercise.py

**Check output**

Run:
- ls /tmp/spark_output

Expected folders:
- result1
- result2
- result3
- result_pq








