# 📊 McDonalds Stream Data Ingestion Project

This is the workflow oar architecture of the Project:
<img width="944" height="631" alt="image" src="https://github.com/user-attachments/assets/7dc0c85c-5f23-4042-81ed-4fc51073e9b1" />

1️⃣Data Sources -> Kafka Topics
Two kinds of mock data are produced  (orders and payments)

2️⃣Kafka -> ksqlDB Streams
Inside ksqlDB you turn raw Kafka topics into STREAMS

3️⃣Joining the Streams
ksqlDBperforms a real-time JOIN on a shared key: ✅Typically order_id

4️⃣Write the Joined Output Back to Kafka
The joined stream is written into a new Kafka topic: 👉JoinedDB, This is your **enriched, analytics-ready stream**

5️⃣Kafka Connect Syncs Output into MongoDB
- Kafka Connect runs a MongoDB Sink Connector, configured to watch: 👉Kafka topic JoinedDB
- Anything placed in that topic gets written into: 📝MongoDB Collection (e.g. orders)

6️⃣MongoDB as Analytical Storage
- Now MongoDB stores full enriched documents:

<img width="690" height="195" alt="image" src="https://github.com/user-attachments/assets/2aec4c7b-e236-4fda-92d4-2cc40d2304e6" />

- This becomes the real-time persistent store.

7️⃣Dashboard/ BI / Analytics
Finally, your BI Dashboard tool (Tableau, PowerBI, Grafana, etc) reads from: 👉MongoDB

To show:
- 📊 Orders per hour
- 💰 Revenue by city
- 🍔 Top menu items
- 🏪 Store performance

🎯 Full Flown Summary

<img width="341" height="337" alt="image" src="https://github.com/user-attachments/assets/5d8d0d6c-e138-475c-b09d-24e846375771" />

🧠 What is Demostrated
- ✅Event ingestion
- ✅Stream processing (ksqlDB)
- ✅Real-time joins
- ✅Topic-to-topic data movement
- ✅NoSQL sink (MongoDB)
- ✅Ready for BI reporting
- ▶️All in real time

<img width="579" height="458" alt="image" src="https://github.com/user-attachments/assets/92a6d8ee-e962-440b-8bdf-8dd99f0a62a2" />

🧠Why Time Matters
- Streams represent live events arriving over time.
- If you JOIN orders-payments as soon as the order arrives, the payment might not exist yet -> JOIN fails temporarily

We solve this using a Time Window Join "Within 5 minutes"

<img width="451" height="273" alt="image" src="https://github.com/user-attachments/assets/51f0ddf1-6de3-4d13-8ab5-57f0bcf03b5d" />

📦At 10:06, events arrives in **orders_stream**. Payment not here yet -> JOIN cannot happen, temporary miss

📦At 10:07, event arrives in **payments_stream**

Now ksqlDD checks its 5-minute window:
- Order came at 10:06
- Payment came at 10:07
- Difference = 1 minute -> valid

👉JOIN produces:
<img width="216" height="68" alt="image" src="https://github.com/user-attachments/assets/cd09521a-4dab-44c5-b950-143dda9ed72d" />

🎯 Key Takeaways
- ✅Streams dont arrive at the same time. Real systems are asynchronous

- ✅ksqlDB window JOIN waits for related events. You can define:
WITHIN 5 MINUTES
WITHIN 1 HOUR
BEFORE, AFTER, BETWEEN

- ✅The JOIN result appears only when both streams have matching keys inside the window

⭐ This is exactly how Uber eats, McDonalds, Doordash, Amazon, etc, correlate:
- Orders
- Payments
- Delivery events
- Refunds
All arriving at different moments!

---------------------------------------------------------------------------------------------------------

<img width="630" height="436" alt="image" src="https://github.com/user-attachments/assets/bc2e264e-07f1-42bc-b085-60f49f41b18e" />

Install MongoDB Atlas Database Multi Cloud Database Service.

That “MongoDB_Setup / MongoDB Atlas Database Multi Cloud Database Service” material is showing you how to create a cloud MongoDB database in Atlas and prepare it so your Kafka / KqlDB pipelines can write into it. 

The steps are basically: create an Atlas cluster → open network access → create DB user → get connection string → use it from your tools / code.

Let’s go through it step by step: what, how, and why.

1. **Create a MongoDB Atlas account & project**

What: Sign up or log in to MongoDB Atlas and create a project.

How

- Go to the Atlas website and sign in
- Click New Project → give it a name (e.g. Kafka_McDonalds)

Why

- A project is the logical container where your clusters (databases), users and network settings live. You need this before you can create any MongoDB database.


2. **Create a free/shared cluster (the actual database server)**

What

Create a multi-cloud hosted MongoDB cluster (the “Database Multi Cloud Service” mentioned in your notes).

How

- Inside the project click Build a Database
- Choose Free / Shared (M0) or a small paid tier
- Pick a cloud provider + region (AWS/GCP/Azure, usually same region as your Kafka cluster)
- Cluster name, 'mongo-db-cluster'
- Click Create

Why

This cluster is where your collections will live, and eventually where Kafka Connect MongoDB Sink will write the joined stream (like JoinedDB from your McDonald’s diagram) into a collection for dashboards.














