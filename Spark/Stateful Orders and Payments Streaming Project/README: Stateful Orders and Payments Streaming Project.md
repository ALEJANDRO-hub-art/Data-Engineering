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

Open Confluent Cloud

Open your Kafka cluster

Go to Topics
- Click Create topic
 - Create: orders_topic_data_v1
 - Create another topic: payments_topic_data_v1

















