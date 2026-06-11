I have this project Stateful Orders and Payments Streaming Project

<img width="677" height="217" alt="image" src="https://github.com/user-attachments/assets/7cba3576-1ac4-4910-9439-c255d494ca3a" />

**What the project does**

It has 3 files:

orders_producer.py
- Sends fake order events into Kafka topic: orders_topic_data_v1

payments_producer.py
- Sends fake payment events into Kafka topic: payments_topic_data_v1

join_stream(1).py
- Uses Spark Structured Streaming to read both Kafka topics, join orders with payments by order_id, then write the joined result to MongoDB.

<img width="742" height="378" alt="image" src="https://github.com/user-attachments/assets/b1482eee-c293-4fa7-9a2a-fdec1f4d1851" />

**Create Kafka topics in Confluent Cloud**

In Confluent Cloud GUI:
- Open Confluent Cloud
- Open your web browser.

Go to:
- https://confluent.cloud

Click Sign In. Enter your Confluent Cloud credentials.

Click Continue.

**Open your Kafka cluster**

After logging in:

You will land on the Environments page. Locate the environment used for this project (for example, Default).
- Click the environment name.

You should now see something similar to:

Environment
└── Cluster Name

Under Kafka clusters, click your cluster.

Example:
- Basic Cluster or
- inventory-cluster

Go to **Topics**

Open the Topics Page

Inside the cluster: Create the First Topic

On the Topics page:

Click the blue button:
- Create topic

(usually located in the upper-right corner)

**Configure the First Topic**

A panel called Create topic opens.

Fill in the fields exactly as follows:

Topic name
- Enter: orders_topic_data_v1

Partitions
- Leave the default value: 6

Cleanup policy
- Leave as: Delete

Retention time
- Leave the default setting.

Advanced settings
- Do not modify anything.

Then click:

- Create with defaults or
- Create topic

(depending on your Confluent Cloud version).

Wait a few seconds until the topic status becomes: Provisioned

**Create the Second Topic**

While still on the Topics page:

Click:
- Create topic

Fill in:
- Topic name: payments_topic_data_v1

Partitions
- Leave: 6

Cleanup policy
- Leave: Delete

Then click: 
- Create with defaults or
- Create topic

**Verify Both Topics Exist**

You should now see both topics listed under Topics:

<img width="521" height="117" alt="image" src="https://github.com/user-attachments/assets/9882eddc-1dde-4205-8bf4-315040b24e76" />













