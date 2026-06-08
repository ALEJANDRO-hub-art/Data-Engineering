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

1. Kafka Producer in Python
- Develop a Python script to act as a Kafka producer.
- Use Pandas to read logistics data from a CSV file.
- Serialize the data into Avro format and publish it to a Confluent Kafka topic.


2. Schema Registry Integration
- Establish a Schema Registry for managing Avro schemas.
- Ensure that the Kafka producer and consumer fetch the schema from the Schema Registry during serialization and deserialization.


3. Logistics Data Information
- Logistics data contains fields like (e.g., shipment details, tracking information).
