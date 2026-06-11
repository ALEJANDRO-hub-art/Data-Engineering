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
- Enter: **orders_topic_data_v1**

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
- Topic name: **payments_topic_data_v1**

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

Now that we have created Kafka topics lets:

**Create MongoDB Atlas database**

In MongoDB Atlas GUI:

Open MongoDB Atlas, Open your cluster

Click: Browse Collections

Click: Create Database

Database name: **ecomm_mart**

Collection name: **orders_data_process_fact**

This matches the Spark output settings in join_stream.py.

**A more specific step procedure Create MongoDB Atlas Database (Exact GUI Steps)**

*Open MongoDB Atlas*

Open your web browser. Go to:

- https://cloud.mongodb.com

Click Sign In.

Enter your MongoDB Atlas credentials.

Click Sign In.

*Open Your Cluster*

After logging in: You will arrive at the Projects page.

- Click the project used for this assignment. Example: Ecommerce Project

In the left menu, click:

- Database or
- Database Deployments

(depending on your Atlas version).

Under Database Deployments, locate your cluster.

Example: Cluster0
 
- Click the cluster name.

You should now see your cluster dashboard.

*Open Browse Collections*

Inside the cluster page:

Locate the button:
- Browse Collections. Click Browse Collections.

The navigation path becomes:

MongoDB Atlas
- → Project
- → Database Deployments
- → Cluster0
- → Browse Collections
 
**Create the Database**

Inside Collections:

If this is your first database, click:
- Add My Own Data

If databases already exist:

Click the green button:
- Create Database

located near the upper-right corner. A window titled Create Database appears.

**Enter the Database Name**

In the popup window: Database Name

Type exactly:
- ecomm_mart
- 
**Enter the Collection Name**

Under Collection Name, type exactly:
- orders_data_process_fact

Your form should look like this:

<img width="492" height="125" alt="image" src="https://github.com/user-attachments/assets/0368e5fc-ca5d-4a70-bfd0-3d9c24129b6d" />

**Create the Database**

Verify the names are correct.

Click the green button:
- Create

MongoDB Atlas will create: 

<img width="255" height="67" alt="image" src="https://github.com/user-attachments/assets/04c364d2-4762-4021-81d5-f75ccbd52d6d" />


**Verify the Database Was Created**

You should now see the following structure in the left panel:

<img width="261" height="55" alt="image" src="https://github.com/user-attachments/assets/7f758882-ee8a-4365-b45b-f4cd04b1c703" />

Click: **orders_data_process_fact**

The collection will open.

Initially, you will see:

No documents found.

This is normal because Spark has not written any records yet.

**Final MongoDB Atlas Structure**

After completing this step, your Atlas database should look exactly like this:

<img width="293" height="69" alt="image" src="https://github.com/user-attachments/assets/19baff38-bad4-48f4-b4b3-2c6d43236df1" />

This matches the MongoDB output settings used in the Spark script (join_stream.py). When you run the Spark streaming job later, the processed records will automatically be inserted into:

<img width="313" height="54" alt="image" src="https://github.com/user-attachments/assets/c5b06c2b-97d6-4366-982d-2078fff88da3" />

**Open Windows Prompt cmd in the project folder**

Do:
- cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 5\1 Class Content PPT, Notes, Exercises DONE\Kafka-To-Mongo-Spark-Streaming DONE"

**Install Python dependency for producers**

Run:
- pip install kafka-python

**Start the Spark streaming job**

Run this first:
- spark-submit join_stream.py

This starts Spark and waits for new Kafka messages.

Leave this CMD window open.

Lets inspect this **join_stream.py**
- Defines schemas for orders and payments
- Read orders stream
- Read payments stream
- Combine streams
- Apply stateful processing with applyInPandasWithState








