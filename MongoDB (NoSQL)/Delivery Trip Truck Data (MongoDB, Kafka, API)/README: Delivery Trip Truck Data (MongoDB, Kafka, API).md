## 📊 Delivery Trip Truck Data (MongoDB, Kafka, API) Project.

### 📝 MongoDB Assignment

### 📝 Assignment: Integrating MongoDB with Kafka using Python


### 📘 Objective:
Develop a Python-based application that integrates Kafka and MongoDB to process logistics data. The application will involve a Kafka producer and consumer, data serialization/deserialization with Avro, and data ingestion into MongoDB. Additionally, an API will be developed to interact with the data stored in MongoDB.


### 📋 Requirements:
- Basic understanding of Python, Kafka, MongoDB, and Docker.
- Access to Confluent Kafka and MongoDB Atlas.
- Familiarity with Docker and containerization.

### 📋 Tasks

**1. Kafka Producer in Python**
- Develop a Python script to act as a Kafka producer.
- Use Pandas to read logistics data from a CSV file.
- Serialize the data into Avro format and publish it to a Confluent Kafka topic.

**2. Schema Registry Integration**
- Establish a Schema Registry for managing Avro schemas.
- Ensure that the Kafka producer and consumer fetch the schema from the Schema Registry during serialization and deserialization.

**3. Logistics Data Information**
- Logistics data contains fields like (e.g., shipment details, tracking information).

**4. Kafka Consumer in Python**
- Write a Python script for the Kafka consumer.
- Deserialize the Avro data and ingest it into a MongoDB collection.

**5. Scaling Kafka Consumers**
- Utilize Docker to scale Kafka consumers.
- Provide instructions for deploying multiple instances of the Kafka consumer using Docker.

**6. Data Validation in Kafka Consumer**
- Implement data validation checks in the consumer script before ingesting data into MongoDB.
- Validations like checking for null values, data type validation, and format checks.
- More assumptions can be taken for data validation, make sure to list down your assumptions in the submission document.

**7. API Development using MongoDB Atlas**
- Create an API to interact with the MongoDB collection.
- Implement endpoints for filtering specific JSON documents and for aggregating data.
- More assumptions & use-cases can be considered for API creation, make sure to list down your assumptions & use-cases in the submission document.

**8. Deliverables**
- Python scripts for Kafka producer and consumer.
- Sample logistics data CSV file.
- Dockerfile for scaling Kafka consumers.
- API code for MongoDB interactions.
- Documentation explaining the setup and execution of the application.

--------------------------------------------------------------------------------------------------------------------

### Solution
The following are the Project files.

<img width="839" height="289" alt="image" src="https://github.com/user-attachments/assets/09727bc0-b8bb-4209-bb2a-7e96bc62b7b1" />

The website GUI for this project is mainly:

- Confluent Cloud: Kafka topic + Schema Registry
- MongoDB Atlas: MongoDB database/collection
- Docker Desktop: run the consumer container
- Your browser/Postman: test the API endpoints

Important: your files contain hardcoded passwords/API keys. Rotate them before publishing to GitHub.

**1. What each uploaded file does**

**logistics_data_producer.py**
Reads delivery_trip_truck_data.csv, serializes rows with Avro, and publishes them to the Kafka topic logistics_data.

**logistics_data_consumer.py**
Consumes Avro messages from Kafka topic logistics_data, validates bookingID, and inserts valid records into MongoDB collection gds_db.logistics_data.

**logistics_data_api1.py**
Flask API on port 5000. Endpoint:
/api/filter?vehicle_no=KA590408
Filters MongoDB records by vehicle number.

**logistics_data_api2.py**
Flask API on port 5001. Endpoint:
/api/count
Counts vehicles grouped by GpsProvider.

**Delivery_trip_truck_data Sample.txt**
Shows the expected CSV columns and sample logistics data rows.

**Dockerfile**
Builds a Python container for the Kafka consumer.

**docker-compose.yml**
Runs the consumer container with Kafka environment variables.

**2. GUI setup steps**

MongoDB Atlas GUI

Website:

<img width="200" height="42" alt="image" src="https://github.com/user-attachments/assets/564d877b-75be-4ee5-8294-14668b003b00" />


Steps:

**1. Sign in to MongoDB Atlas.**
**2. Create a Project.**
**3. Create a free cluster.**

Click:
Build a Database

Select:
M0 Sandbox (FREE)

Provider:
AWS

Region:
Closest to you

Cluster Name:
logistics-cluster

Click:
Create Deployment

**4. Go to **Database Access.****

**5. Create a database user.**
After cluster creation Atlas shows:
Security Quickstart

Click:
Username
Example:
admin

Password:
Password123!
(or your own)

Click:
Create User

**6. Go to **Network Access.****

Atlas asks:
Where would you like to connect from?

Select:
My Local Environment

Click:
Add Current IP Address

For testing you may use:
0.0.0.0/0

Click:
Finish and Close

**7. Add your IP address, or temporarily use:**
**8. Go to **Database → Connect → Drivers.****
**9. Copy your MongoDB connection string.**

Left Menu:
Database

Click your cluster.

Click:
Connect

Select:
Drivers

Select:
Python

Copy:

<img width="296" height="32" alt="image" src="https://github.com/user-attachments/assets/f159a6c6-d1de-42f0-86d0-4dc44fc3acf7" />

Your uploaded files already contain a connection string here:

<img width="426" height="84" alt="image" src="https://github.com/user-attachments/assets/a73c5ecc-f3f7-4136-b62c-e3c99b64c86f" />


**10. Database name used by your code:**

gds_db

**11. Collection name used by your code:**

logistics_data

Open:
Database

Click:
Browse Collections

Click:
Add My Own Data

Database Name:
gds_db

Collection Name:
logistics_data

These names come directly from your code.

Click:
Create

Verify Database. You should now see:

gds_db
   └── logistics_data

Currently:

0 Documents

This is normal.

**3. Confluent Cloud GUI**

Website:

https://confluent.cloud

Steps:

**1. Sign in to Confluent Cloud.**
**2. Create an environment.**
After login:
Left Menu:
Environments

Click:
+ Add Environment

Fill:
Environment Name:
Logistics-Project

Click:
Create

**3. Create a Kafka cluster.**

Inside your environment:

Click:
Create Cluster

Select:
Basic Cluster

Provider:
AWS

Region:
us-east-2
(Your code points to AWS Ohio endpoints.)

Cluster Name:
logistics-cluster

Click:
Launch Cluster

Wait 2–5 minutes.

**4. Create a topic named:**
logistics_data

Left Menu:
Cluster Overview

Click your cluster.

Left Menu:
Topics

Click:
Create Topic

Topic Name:
logistics_data

Partitions:
6

Cleanup Policy:
Delete

Retention:
Default

Click:
Create Topic

Your producer sends to this topic.

Your consumer subscribes to this topic.

**5. Go to **API Keys.****
**6. Create Kafka API key and secret.**

Left Menu:
API Keys

Click:
Create Key

Select:
Global Access
or
Kafka Cluster Access

Choose:
logistics-cluster

Click:
Next
Create API Key

You will receive:
API Key
API Secret

Example:
ABC123XYZ
and
SecretValue

Save your Credentials

Click:
Download and Continue

Save the file.

You will later replace:
**sasl.username**
**sasl.password**

inside:

logistics_data_producer.py

and

logistics_data_consumer.py

**Open Cluster Settings**

Left Menu:
Cluster Overview

Click:
Cluster Settings

Locate:
Bootstrap Server
Example:
pkc-xxxxx.us-east-2.aws.confluent.cloud:9092

Copy it.

Replace:
bootstrap.servers

inside producer and consumer if needed.

**7. Go to **Schema Registry.****

Left Menu:
Schema Registry

If Schema Registry is not enabled:

Click:
Enable Schema Registry

Choose:
AWS

Same region as cluster.

Click:
Continue

Wait until deployment finishes.

**8. Create Schema Registry API key and secret.**

**Create Schema Registry API Key**

Inside:
Schema Registry

Click:
API Keys

Click:
Create API Key

Select:
Global Access

Click:
Create

You receive:
Schema Registry Key
Schema Registry Secret

Save them.

**Create Schema**

Left Menu:
Schema Registry

Click:
Schemas

Click:
Add Schema

**9. Register an Avro schema with subject:**

logistics_data-value

The producer and consumer both expect that schema subject.

**Select Subject**

Subject:
logistics_data-value

This must exactly match your producer and consumer code.

**Select Format**

Format:
Avro

Click:
Continue

**Paste Avro Schema**

Paste your Avro schema JSON.

Example:

<img width="474" height="312" alt="image" src="https://github.com/user-attachments/assets/98bdb4ce-d837-4847-a358-b1692a393651" />

For your project you should include all CSV fields from the logistics dataset.

Click:
Validate

Then:
Register

**Verify Schema**

You should now see:

Schemas
 └── logistics_data-value
       └── Version 1

**Execution steps**

Open CMD or PowerShell inside your project folder:

cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\6 MongoDB (NoSQL)\Module 4 - MongoDB Class 2\2 Class Assignment and Solutions\MongoDB Assignment  1 Solution"

Install packages:

pip install pandas pymongo flask confluent-kafka fastavro requests

Run producer:

python logistics_data_producer.py

Expected result: records are published to Kafka topic logistics_data.

Run consumer:

python logistics_data_consumer.py

Expected result: records are consumed from Kafka and inserted into MongoDB.

Run API 1:

python logistics_data_api1.py

Test in browser:

http://localhost:5000/api/filter?vehicle_no=KA590408

Run API 2 in another terminal:

python logistics_data_api2.py

Test in browser:

http://localhost:5001/api/count

**Docker execution**

Build image:

docker build -t consumer_image .

Run with Docker Compose:

docker compose up

This runs the Kafka consumer inside Docker.

**Docker Execution — Exact GUI Steps (Windows + Docker Desktop)**

This section starts after you have already completed:

✅ MongoDB Atlas setup
✅ Confluent Cloud setup
✅ Downloaded all project files
✅ Installed Docker Desktop

Your Docker container will run the Kafka Consumer that reads from the logistics_data topic and writes into MongoDB Atlas.

**Step 1 — Verify Docker Desktop is Running**

Open:
Start Menu
→ Docker Desktop

Wait until Docker starts.

You should see:
Docker Desktop
Status: Engine running

Green indicator:
Running


**Step 2 — Open Project Folder**

Create a folder:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\6 MongoDB (NoSQL)\Module 4 - MongoDB Class 2\2 Class Assignment and Solutions\MongoDB Assignment  1 Solution

Copy these files into it:

Dockerfile
docker-compose.yml

logistics_data_consumer.py
logistics_data_producer.py

logistics_data_api.py
logistics_data_api2.py

delivery_trip_truck_data.csv

Your consumer is the main process Docker will run.

<img width="794" height="331" alt="image" src="https://github.com/user-attachments/assets/78978451-6c92-451f-9cc2-7d3a27aa2030" />

**Open Command Prompt**

Press:
Windows Key + R

Type:
cmd

Click:
OK

**Navigate to Project Folder**

Example:
cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\6 MongoDB (NoSQL)\Module 4 - MongoDB Class 2\2 Class Assignment and Solutions\MongoDB Assignment  1 Solution"

Verify:
dir

You should see:
Dockerfile
docker-compose.yml
logistics_data_consumer.py
...

**Build Docker Image**

Inside Command Prompt:
**docker build -t consumer_image**

Explanation:
docker build     = create image
-t               = image tag
consumer_image   = image name
.                = current folder

Expected:
Successfully built xxxxx
Successfully tagged consumer_image:latest

**Verify Image in Docker Desktop GUI**

Open:
Docker Desktop

Left Menu:
Images

You should see:
consumer_image
latest

**Verify Image from CLI**

Run:
docker images

Expected:
REPOSITORY        TAG
consumer_image    latest

**Start Docker Compose**

In the same Command Prompt:

docker compose up
or
docker-compose up

Docker Compose reads:
docker-compose.yml

and starts the services.

**Verify Containers in Docker Desktop GUI**

Open:
Docker Desktop

Left Menu:
Containers

You should now see something similar:
logistics-consumer

Status:
Running

Green icon:
● Running

**View Container Logs in GUI**

Click:
Containers
→ logistics-consumer

Click:
Logs

You should see:
Received message ...
Inserted message into MongoDB ...

These messages come from your Kafka Consumer.

**Verify Kafka Messages Arrive**

Open:
Confluent Cloud

Navigate:

Environment
- Cluster
- Topics
- logistics_data
- Messages

You should see records arriving from the producer.

**Verify MongoDB Documents**

Open:
MongoDB Atlas

Navigate:
Database
- Browse Collections
- gds_db
- logistics_data

You should now see documents inserted by the consumer.

**Keep Docker Running**

Leave this window open:

docker compose up

*If you close it, the container stops.*

**Run in Background (Optional)**

Instead of:

docker compose up

Use:

docker compose up -d

Meaning:

-d = detached mode

**Container continues running after closing the terminal.**

**Verify Running Containers**

Run:
docker ps

Expected:
CONTAINER ID
IMAGE
consumer_image
STATUS Up

**Stop Containers**

To stop:
docker compose down

Expected:
Stopping containers...
Removing containers...

<img width="590" height="207" alt="image" src="https://github.com/user-attachments/assets/6a8981d1-40cc-41af-9cae-a74a0fd1a273" />

<img width="596" height="417" alt="image" src="https://github.com/user-attachments/assets/818f0d12-f1c2-4d37-986c-08f1145ce993" />





