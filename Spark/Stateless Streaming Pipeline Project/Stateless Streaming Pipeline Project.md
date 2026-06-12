I have the following project Stateless Streaming Pipeline Project.

<img width="813" height="225" alt="image" src="https://github.com/user-attachments/assets/c3864462-ef41-4f1d-9f5f-a2534b70bdda" />

It has 3 files:

**user_data.json**
- Sample user records: id, name, age.

**user_data_producer.py**
- Kafka producer. It reads user_data.json and publishes each record to Kafka topic **user_data_topic.**

**kafka_spark_stateless_streaming.py**
- Spark Structured Streaming job. It reads from Kafka, parses JSON, filters users where age > 25, and prints results to console.

**Important:** your Kafka API key/password are inside the code. Rotate/delete that key in Confluent Cloud after testing.

<img width="724" height="329" alt="image" src="https://github.com/user-attachments/assets/ae9066d9-f783-4942-b6e7-66da9549e330" />

**Where to download/place all files**

Create this folder on Windows:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 5\1 Class Content PPT, Notes, Exercises DONE\Stateless_Streaming_Pipeline DONE

Put all 3 files inside that folder:

Kafka_Spark_Stateless_Streaming/
│
├── kafka_spark_stateless_streaming.py
├── user_data_producer.py
└── user_data.json

In our case the project name is:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 5\1 Class Content PPT, Notes, Exercises DONE\Stateless_Streaming_Pipeline DONE

The producer expects the file name to be exactly: **user_data.json**

**Step-by-step execution**

**Create Kafka topic in Confluent Cloud GUI**

Open Confluent Cloud.

Open your Kafka cluster.
Go to Topics. Click Create topic.
- Topic name: user_data_topic
- Partitions: 1

Click Create with defaults.

Lets explain it in detail. Open Your Kafka Cluster

After logging in:

On the left menu, click Environments. Select the environment that contains your Kafka cluster (for example, "Default").

Under Clusters, you will see your Kafka cluster listed. Example:
- Basic Cluster or
- Development Cluster

Click the cluster name.

You are now inside the Kafka cluster dashboard.

Open the Topics Page

Inside the cluster: Look at the left navigation menu.
- Click: Topics

The screen will show all existing Kafka topics. Example:

Topics
- orders
- payments
- inventory

Create a New Topic. In the upper-right corner: Click the blue button:
- Create topic

A "Create Topic" panel/window opens.

Enter the Topic Name. You will see a field labeled:

- Topic name. Click inside the box and type exactly: **user_data_topic**

It should look similar to this:

Topic name
┌─────────────────────┐
│ user_data_topic     │
└─────────────────────┘

Set the Number of Partitions. Below the topic name field, locate:

Partitions. Delete the existing value if necessary.
- Type: 1

It should appear as: Partitions: 1

Leave all other settings unchanged.

Create the Topic. At the bottom of the page:
- Click: Create with defaults; or sometimes simply: Create

Confluent Cloud will now create the topic.

Verify the Topic Was Created

After a few seconds: You will automatically return to the Topics page. Look for the new topic in the list.

You should see:

<img width="733" height="117" alt="image" src="https://github.com/user-attachments/assets/94921757-2fc9-4701-8f30-a562dc2e9826" />

What you just created. You created a Kafka topic called:
- user_data_topic

with:
- Partitions: 1
- Replication factor: Confluent Cloud default
- Retention settings: Confluent Cloud defaults

This topic will be used by your producers to publish user data messages and by consumers to read those messages later in the project.

**Create/confirm API key in Confluent GUI**

Open your Kafka cluster.

Go to API keys. Create an API key.

Copy:
- Bootstrap server
- API key
- API secret

These values are used in both Python files.

**Upload/create GCS checkpoint bucket**

The Spark file uses this checkpoint path: **gs://streaming_checkpointing/stateless_processing**

In Google Cloud GUI:

Open Google Cloud Console.

Go to Cloud Storage.

Click Create bucket. Bucket name:
- **streaming_checkpointing**
 
Choose region.

Click Create.

Inside the bucket, create folder:
- **stateless_processing/**

Open Windows Command Promp (cmd) in the project folder:

Do:

cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 5\1 Class Content PPT, Notes, Exercises DONE\Stateless_Streaming_Pipeline DONE"

**Install producer dependency**

Run:
- pip install confluent-kafka

**Run Kafka producer**

Run:
- python user_data_producer.py

This sends each JSON record to Kafka every 4 seconds.

**Run Spark streaming job**

Use Spark submit:
- spark-submit kafka_spark_stateless_streaming.py

The output will show only users with: age > 25

So users like John, Doe, Alice, Charlie, David, Eva, Frank, and Grace should appear.

## GUI execution summary

**Confluent Cloud GUI**

Use it for:
- Create cluster → Create topic → Create API key → Monitor messages

**Google Cloud GUI**

Use it for:
- Create Cloud Storage bucket → Create checkpoint folder
 
**Windows GUI**

Use it for:
- Create project folder → Put files inside → Open CMD from folder

**CMD / Terminal**

Use it for:
- Run producer
- Run Spark streaming job

**Workflow in simple words**
- The JSON file is your source data.
- The producer sends that data into Kafka.
- Spark reads the Kafka stream live.
- Spark filters users older than 25.
- The filtered stream prints to the console.








