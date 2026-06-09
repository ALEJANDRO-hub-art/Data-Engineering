I have the following project **Cassandra (NoSQL Database) Ecommerce-orders Analytics Project.**

<img width="718" height="309" alt="image" src="https://github.com/user-attachments/assets/dbc58f0c-6b4a-4e5b-a350-2e74851c374a" />

**Assignment Overview**

The aim of this assignment is to create a real-time data pipeline for processing **e-commerce** data using Apache Kafka and Apache Cassandra. You will ingest data from a CSV file using a Kafka producer, transform the data using a Kafka consumer, and finally store the processed data in a Cassandra table.

**Problem Statement**

Imagine you're part of the data engineering team at a large e-commerce company. Your company receives real-time data related to customer orders. This data is crucial for various business operations, including inventory management, customer service, and business analytics.

The data is received in CSV format and needs to be processed in real-time to extract valuable insights.

**Assignment Steps**

**1. Dataset**

   Load the 'olist_orders_dataset.csv' into a pandas dataframe and examine its structure and contents.

**2. Apache Kafka Setup**

   Install and configure Apache Kafka on your system. Create a Kafka topic, named 'ecommerce-orders', to hold the e-commerce data.

**3. Kafka Producer**

   Develop a Kafka producer in Python that reads the data from the pandas dataframe and publishes it to the 'ecommerce-orders' Kafka topic. The key for each message should be a combination of the 'customer_id' and 'order_id' fields from the dataset.

**4. Apache Cassandra Setup**

Install and set up Apache Cassandra. Create a **keyspace**, named **'ecommerce'**, for storing the e-commerce data.

**5. Cassandra Data Model**

Design a table, named **'orders'**, within the **'ecommerce'** keyspace. This table should reflect the schema of the incoming data and include additional columns for the derived features:

**'OrderHour'** and **'OrderDayOfWeek'.**

The data model should have **'customer_id'** as the partition key and **'order_id'** and **'order_purchase_timestamp'** as clustering keys.

- CREATE TABLE ecommerce.orders (
    - order_id uuid,
    - customer_id uuid,
    - order_status text,
    - order_purchase_timestamp timestamp,
    - order_approved_at timestamp,
    - order_delivered_carrier_date timestamp,
    - order_delivered_customer_date timestamp,
    - order_estimated_delivery_date timestamp,
    - OrderHour int,
    - OrderDayOfWeek text,
    - PRIMARY KEY ((**customer_id**), **order_id**, **order_purchase_timestamp)**
- );

**6. Kafka Consumer and Data Transformation**

Develop a Kafka consumer (make sure to have a consumer group) in Python that subscribes to the **'ecommerce-orders'** topic. The consumer should derive two new columns **'PurchaseHour'** and **'PurchaseDayOfWeek'**, then ingest transformed data into the **'orders'** table in Cassandra.

**7. Quorum Consistency**

While inserting data into the Cassandra 'orders' table, ensure that the write operations maintain quorum consistency.

**8. Testing**

Test your data pipeline end-to-end. Run your Kafka producer to ingest the data, then execute the Kafka consumer to process the data and insert it into the Cassandra table. Verify the data in the Cassandra table matches the processed data and that all transformations have been executed correctly.

**9. Assignment Submission**

Submit your Python scripts for the Kafka producer and consumer, the CQL commands used to create the keyspace and table in Cassandra, and a detailed report explaining the pipeline, any challenges faced, and how they were addressed.


--------------------------------------------------------------------------------------------------------------------------

### Project goal

This project is a real-time e-commerce orders pipeline:

**CSV file → Kafka Producer → Kafka topic ecommerce-orders → Kafka Consumer → Cassandra table ecommerce.orders**

The assignment specifically asks you to load olist_orders_dataset.csv, publish records to Kafka, consume them, transform timestamps into hour/day fields, and insert them into Cassandra with quorum consistency.

<img width="637" height="562" alt="image" src="https://github.com/user-attachments/assets/d86a3f71-ff3d-433d-8a99-c5f0a8ad67e1" />

<img width="658" height="455" alt="image" src="https://github.com/user-attachments/assets/0de453ea-d895-4486-8793-27f4fa533b79" />

Inside the **consumer.py** we have it here:

<img width="616" height="381" alt="image" src="https://github.com/user-attachments/assets/89b7174b-46aa-4caa-861d-adf8f6f1bbef" />

Inside the **cassandra_table_create.py** we have it here:

<img width="667" height="445" alt="image" src="https://github.com/user-attachments/assets/34286496-e92e-4f63-86f9-719d4bd67bbf" />

<img width="645" height="519" alt="image" src="https://github.com/user-attachments/assets/428b0df2-c716-40f4-9636-2d851b22b9a0" />

<img width="643" height="506" alt="image" src="https://github.com/user-attachments/assets/32d75727-2342-4d95-a8c6-2f866fa975d8" />

Inside the **DataStax Astra CQL Console**, there is no cd command.

The CQL Console is not a Windows/Linux terminal. It is a database query editor that only accepts CQL (Cassandra Query Language) commands.

**4. Kafka / Confluent Cloud GUI steps**

Go to Confluent Cloud

Sign in

Create or open your Kafka cluster:

If You Do NOT Have a Kafka Cluster Yet

Step 1: Create Environment

Sign in to Confluent Cloud.

Click Environments (left menu).

Click Create Environment.

Enter:

- Environment Name:Kafka-Cassandra-Demo

Click Create.

Step 2: Create Kafka Cluster

Inside the environment click:

Create Cluster

Select: Basic Cluster

(Free tier is usually sufficient for this assignment.)

Choose:

- Cloud Provider: AWS

Choose a region closest to you, for example: us-east-1

Click: Continue

Review settings.

Click: Launch Cluster

Wait 2–5 minutes.

Status changes:

- Provisioning
- ↓
- Ready
- 
Step 3: Open the Cluster

When status shows Ready:

- Click the cluster name.
- The Kafka Cluster Dashboard opens.
- You are now inside the cluster.

You should see:

- Overview
- Topics
- Clients
- Schema Registry
- Connectors
- Metrics

DONE with 'Create or open your Kafka cluster:'

Go to Topics

Click Create topic

Topic name:ecommerce-orders

Partitions: 1 is okay for testing

Click Create with defaults

**Schema Registry**

Your producer and consumer use Avro Schema Registry. They fetch this subject:

**ecommerce-orders-value**

So in Confluent Cloud:

Go to **Schema Registry**

Make sure Schema Registry is enabled

Go to topic **ecommerce-orders**

Add/register a value schema matching the CSV fields:

<img width="596" height="270" alt="image" src="https://github.com/user-attachments/assets/8a6773af-4f72-450e-b695-b8d5765ac570" />

**5. Run the project from Windows terminal**

Open Command Prompt or Anaconda Prompt.

*Go to your project folder:*

- cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\7 Cassandra (NoSQL)\Module 4 - Cassandra Class 2\Step 2\Cassandra_Assignment_Solution"

*Install packages:*

- pip install pandas confluent-kafka cassandra-driver

Run Cassandra table creation:

- python "cassandra_table_create.py"

Run the consumer first:

- python "consumer.py"

Leave that window open.

Open a second terminal, go to the same folder:

- cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\7 Cassandra (NoSQL)\Module 4 - Cassandra Class 2\Step 2\Cassandra_Assignment_Solution"

Run the producer:

- python "producer.py"

The producer sends records to Kafka. The consumer receives them and inserts them into Cassandra.

**6. Verify in Cassandra GUI**

In Astra:

Open your database

Click: CQL Console

Run:

- USE ecommerce;

Check rows:

- SELECT * FROM ecommerce.orders LIMIT 10;

Expected result: rows from the CSV with extra transformed columns:

- order_hour
- Oorder_day_of_week

<img width="637" height="501" alt="image" src="https://github.com/user-attachments/assets/3ad6744e-027e-49b0-95d1-6ab70a8a3fb6" />



