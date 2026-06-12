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
















