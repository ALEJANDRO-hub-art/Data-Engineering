# 📊 Kafka Assignment - Real-Time Data Processing with Confluent Kafka, MySQL, and Avro

## 📘 Objective:
In this assignment, you will build a Kafka producer and a consumer
group that work with a MySQL database, Avro serialization, and
multi-partition Kafka topics. The producer will fetch incremental data
from a MySQL table and write Avro serialized data into a Kafka topic.
The consumers will deserialize this data and append it to separate JSON
files.

## 🛠 Tech Stack
Tools Required:
- Python 3.7 or later
- Confluent Kafka Python client
- MySQL Database
- Apache Avro
- A suitable IDE for coding (e.g., PyCharm, Visual Studio Code)

## 📖 Background:
You are working in a fictitious e-commerce company called "BuyOnline"
which has a MySQL database that stores product information such as
product ID, name, category, price, and updated timestamp. The
database gets updated frequently with new products and changes in
product information. The company wants to build a real-time system to
stream these updates incrementally to a downstream system for
real-time analytics and business intelligence.

## 🔄 Steps:

### 🔄 Step 1: MySQL Table Setup  
** Create a table named 'product' in MySQL database with the following columns:**
- ➔ id - INT (Primary Key)
- ➔ name - VARCHAR
- ➔ category - VARCHAR
- ➔ price - FLOAT
- ➔ last_updated - TIMESTAMP

### 🔄 Step 2: Kafka Producer
- Write a Kafka producer in Python that uses a MySQL connector to
fetch data from the MySQL table.
- In your producer code, maintain a record of the last read
timestamp. Each time you fetch data, use a SQL query to get
records where the last_updated timestamp is greater than the last
read timestamp.
- Serialize the data into Avro format and publish the data to a Kafka
topic named "product_updates". This topic should be configured
with 10 partitions.
- Use the product ID as the key when producing messages. This will
ensure that all updates for the same product end up in the same
partition.
- Update the last read timestamp after each successful fetch.

## 🔄 Step 3: Kafka Consumer Group and Data Transformation
- Write a Kafka consumer in Python and set it up as a consumer
group of 5 consumers.
- Each consumer should read data from the "product_updates"
topic.
- Deserialize the Avro data back into a Python object.
- Implement data transformation logic. For example:
- Change the category column to uppercase.
- Apply some business logic to update the price column, such as
applying a discount if a particular product falls under a specific
category.

## 🔄 Step 4: Writing Transformed Data to JSON Files
- Each consumer should convert the transformed Python object into
a JSON string and append the JSON string to a separate JSON
file. Make sure to open the file in append mode.
- Also, ensure each new record is written in a new line for ease of
reading.
- Close the file after writing to make sure all data is saved properly.

## 📦 Deliverables:
- The source code for the Kafka producer and consumer group in
Python.
- SQL queries used for incremental data fetch from MySQL.
- Avro schema used for data serialization.
- Data transformation logic.
- The resulting JSON files with appended records.
- Documentation explaining how to run and test the system.
- Screenshots demonstrating the successful running of your
application.

## ✅ Evaluation Criteria:
Your assignment will be evaluated based on the following:
- Correctness of the Python code.
- Use of Avro for data serialization.
- Successful incremental fetching of data from the MySQL table.
- Successful writing of data to the Kafka topic with proper
partitioning.
- Successful setup of a Kafka consumer group.
- Correct transformation and writing of data to separate JSON files.
- Quality of your documentation.

## 🏆 Bonus Points:
For bonus points, you can also provide:
- A Dockerfile to run your application.
- Unit tests for your Python code.
- Any advanced data processing, like filtering or transforming the
data before sending it to the downstream system.

## 📝 Additional Instructions:
Remember to update your database with new product details while
testing the producer, so that it can fetch incremental data based on the
last_updated timestamp.

------------------------------------------------------------------------------------------------
## 🔄 Step 1
<img width="941" height="484" alt="image" src="https://github.com/user-attachments/assets/191ec40f-69a0-488c-b1f5-77393525535c" />

## 🔄 Step 2
In here we write a ***Kafka producer called avro_data_producer*** Python file (extension .py) with the characteristics asked
above in Step 2 detailed explanation.

<img width="538" height="526" alt="image" src="https://github.com/user-attachments/assets/7d5ac960-4fd0-44dd-b3cc-306df671a18c" />

At beginning of the scrypt you import:
- Utilities.
- confluent_kafka clien libraries.
- mysql.connector for DB connection.
- json for config file.
- AvroSerializer to serialize data to Avro format.

<img width="495" height="292" alt="image" src="https://github.com/user-attachments/assets/e2ab42cc-1777-4b45-8983-d645a4d7278d" />

def delivery_report (err, msg):
This function runs after kafka sends a message.
It prints:
- success - which topic/partition/offset.
- failure - error message.

<img width="517" height="133" alt="image" src="https://github.com/user-attachments/assets/05a29de8-a625-4f05-b976-e70c6aa2ea75" />

kafka_config = { ... }
Here we define how to reach kafka:
- bootstrap server (Confluent Cloud broker).
- SASL username/password
- SSL authentication

<img width="352" height="93" alt="image" src="https://github.com/user-attachments/assets/6f736668-ad0a-4c13-b2a8-5c2cadd48d3b" />

schema_registry_client = SchemaRegistryClient ({...})
Connects to Confluent Schema Registry:
- stores and manages Avro schemas
- validates messages before publishing
- ensures schema evolution compatibility

<img width="327" height="106" alt="image" src="https://github.com/user-attachments/assets/c5b937fe-972e-44e9-b65f-a8aafff1d68d" />
<img width="479" height="177" alt="image" src="https://github.com/user-attachments/assets/b726c7d3-f6cb-4f5f-9bf8-0c060874b8f3" />

Our python scrypt needs to use MySQL connector to fetch data from the MySQL table.
- connection = mysql.connector.connect(...)
	host, user, password, database
- cursor = connection.cursor()

<img width="704" height="387" alt="image" src="https://github.com/user-attachments/assets/69b69596-fb12-41f4-91c1-3a5e7a12ec94" />

<img width="528" height="185" alt="image" src="https://github.com/user-attachments/assets/679e469d-ed52-4cfb-97d3-ad1f31bbb701" />

Fetch Avro Schema
- subject_name = 'product_updates-value'
- schema_str = schema_registry_client.get_latest_version(subject_name).schma.schema_str
This pulls the latest registered schema from Schema Registry.
Is used to serialize message payload correctly.

<img width="503" height="211" alt="image" src="https://github.com/user-attachments/assets/2a400c0d-2891-4269-9f0e-d87a3364544e" />

Create Serializers
- key_serializer = StringSerializer('utf_8')
- avro_serializer = AvroSerializer (...)
Kafka message parts:
- Key - String (typically product ID)
- Value - Avro (JSON compressed + schema validated)

<img width="513" height="291" alt="image" src="https://github.com/user-attachments/assets/7fdd3cbb-3ee8-4841-b363-98a7e4787a25" />

Create Producer
- producer = SerializingProducer({...})
This is the Confluent producer that:
- serializes keys and values
- felivers messages to kafka
- retries automatically on failure

<img width="467" height="490" alt="image" src="https://github.com/user-attachments/assets/a4cd8eb5-f101-4775-81ce-81282f128e6e" />

Load Last Timestamp from File
- with open('config.json')... this file stores the last record processed.
- Example: {"last_read_timestamp": "2024-11-30 14:21:10"}

<img width="480" height="218" alt="image" src="https://github.com/user-attachments/assets/8e8ce606-d9ba-4a0f-be33-16f9d96f0602" />

Fetch Only New MySQL Rows
- query = "SELECT * FROM product WHERE last_updated > '{}'"
- cursor.execute(query)
- rows = cursor.fetchall()

<img width="497" height="367" alt="image" src="https://github.com/user-attachments/assets/e5a76817-686a-4d7a-a466-e6df026dce78" />
<img width="460" height="142" alt="image" src="https://github.com/user-attachments/assets/0e633cd2-89ff-4eda-a803-3f3ab7e74988" />

Produce Each Row to Kafka

Step-by-step:
1. Convert row tuple {"id":...,"name":...}
2. Publish to Kafka topic product_updates
3. Use product ID as key
4. flush() sends buffer immediately
5. Callback prints result

<img width="450" height="319" alt="image" src="https://github.com/user-attachments/assets/e452bfa2-6a86-4563-b617-6d3512a6b216" />
<img width="353" height="136" alt="image" src="https://github.com/user-attachments/assets/c7507223-97f3-47f8-a3dc-3c07fb43f4b5" />

Update Last Processed Timestamp
- cursor.execute("SELECT MAX(last_updated) FROM product")
- max_date = cursor.fetchone()[0]
- config_data['last_read_timestamp'] = max_date_str
- with open("config.json", "w")...

- This writes back the latest timestamp seen into config file.
- Next run will start from this time -> incremental ingestion.

<img width="386" height="99" alt="image" src="https://github.com/user-attachments/assets/79e71847-da57-42c3-a1ba-be97621ccfa0" />

Cleanup
- cursor.close()
- connection.close()

- Close DB resources to avoid leaks.

<img width="484" height="292" alt="image" src="https://github.com/user-attachments/assets/8f82c0b2-bbc9-473a-b3dc-55d8bc48ee96" />


## 🔄 Step 3 and Step 4 combined.
In here we write a ***Kafka consumer called avro_data_consumer*** Python file (extension .py) with the characteristics asked
above in Step 3 and 4 detailed explanation.

🎯 ***Goal of the Script***

This script:
1. Connects to a Confluent Cloud Kafka cluster
2. Reads messages from topic: product_updates
3. Uses Schema Registry + Avro to deserialize records
4. Applies business logic transformations
   - category → lowercase
   - discount price if category = "category a"
5. Writes each consumed JSON record into a local file consumer1.json

<img width="487" height="414" alt="image" src="https://github.com/user-attachments/assets/ae5df808-7c9e-4dd6-9858-aadab23c4b2f" />

Kafka Configuration
Defines 
- Kafka broker URL
- Security & SASL authentication
- Consumer Group id (group31)
- auto.offset.reset='latest' -> start from newest messages

<img width="767" height="92" alt="image" src="https://github.com/user-attachments/assets/4f578a0f-335b-4b65-9053-792c4b6e8772" />
<img width="793" height="179" alt="image" src="https://github.com/user-attachments/assets/5b225a51-d447-4dc6-a694-3e3c867df383" />

- Connects to Confluent Schema Registry
- Loads Avro schema for values so consumer knows how to decode bytes -> dict

<img width="747" height="313" alt="image" src="https://github.com/user-attachments/assets/691278ad-44cf-40cc-83ee-13492a46af39" />

Deserialize the Avro data back into a Python object.
- Keys -> UTF-8 strings
- Values -> Avro serialized -> Python dict

<img width="423" height="142" alt="image" src="https://github.com/user-attachments/assets/606c9dc4-57c3-4f50-b6e2-ba3af6849924" />
<img width="620" height="413" alt="image" src="https://github.com/user-attachments/assets/23c344ac-75a4-4a21-af79-8ffe2470db55" />

Create Consumer
This consumer automatically:
- Reads bystes from Kafka
- Converts them to Pythn objects (dict)
- Handles key/value deserialization internally

<img width="385" height="162" alt="image" src="https://github.com/user-attachments/assets/9272659d-93f0-45fe-b514-602006d26c02" />

JSON doesnt support datetime
So this convers datetime -> YYYY-MM-DDTHH:MM:SS

<img width="374" height="110" alt="image" src="https://github.com/user-attachments/assets/82b8e5fa-2ca2-4458-b944-4f0b9c4ea9cb" />
<img width="321" height="63" alt="image" src="https://github.com/user-attachments/assets/9b57295b-c104-435f-8315-6f0ee17fd3ab" />
<img width="440" height="138" alt="image" src="https://github.com/user-attachments/assets/46abe0d1-bba0-4fc7-a944-8112bc5edc20" />

Output File Setup
Every consumed message will be appended here.

<img width="389" height="269" alt="image" src="https://github.com/user-attachments/assets/79448722-a6c0-480c-af93-2815efa9b35c" />

Subscribe to Topic

<img width="309" height="107" alt="image" src="https://github.com/user-attachments/assets/69bf957d-1eb4-4651-90a7-28a8942a3d9a" />

Infinite Consume Loop
- Polls every second
- msg is None -> no data yet
- msg.error() -> print Kafka error and skip

<img width="409" height="56" alt="image" src="https://github.com/user-attachments/assets/0aff48c4-d481-4da0-b868-92f6afa034f9" />

Change the category column to uppercase

<img width="549" height="318" alt="image" src="https://github.com/user-attachments/assets/26f405bf-cf40-4aa2-8101-ec5aefbcfb90" />

Apply 50% discount to products in category A
(simulate real-time event enrichment)

### Now lets do ***Step 4***

<img width="463" height="138" alt="image" src="https://github.com/user-attachments/assets/ac8c357e-4d0a-4156-b0dd-d425530a763a" />

Converts processed dict -> JSON string

<img width="476" height="291" alt="image" src="https://github.com/user-attachments/assets/164cb27e-e470-4dd9-9c27-81179620616a" />


<img width="338" height="132" alt="image" src="https://github.com/user-attachments/assets/ca8fdd47-7ee9-49ed-adca-6b2c016d12c1" />
<img width="238" height="100" alt="image" src="https://github.com/user-attachments/assets/70ed3f2b-d6e8-4e2f-a3a8-3799fa07e6cc" />

- Ctrl + C stops loop
-consumer.close() commits offsets and closes connection cleanly

<img width="306" height="237" alt="image" src="https://github.com/user-attachments/assets/3cfef494-0d9b-4ba0-9e92-de172c00ff30" />

Now we did the above code for consumer1.json. Now do the same code for consumer2.json, consumer3.json, consumer4.json, consumer5.json.
The code stays the same the only part you need to change is this one:
<img width="454" height="257" alt="image" src="https://github.com/user-attachments/assets/12cb0d22-cb8f-4753-aaae-db5ac25010ba" />

In our project folder we have them here:
<img width="679" height="106" alt="image" src="https://github.com/user-attachments/assets/566fb70b-01aa-42d5-be3e-5ff59c9dedea" />










