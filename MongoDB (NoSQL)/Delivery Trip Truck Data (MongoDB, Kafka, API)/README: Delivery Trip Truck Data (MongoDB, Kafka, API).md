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

1. Sign in to MongoDB Atlas.
2. Create a Project.
3. Create a free cluster.

   Click:
   
<img width="109" height="35" alt="image" src="https://github.com/user-attachments/assets/844b041e-bc8e-43cb-8083-312b02096a42" />

Select:

<img width="130" height="35" alt="image" src="https://github.com/user-attachments/assets/d381ec8a-4dd9-45ae-ac27-fa86a842c043" />

Provider:

<img width="91" height="28" alt="image" src="https://github.com/user-attachments/assets/d6de06a5-ab83-4db9-a9d5-813d0ac1c819" />

Region:

<img width="109" height="38" alt="image" src="https://github.com/user-attachments/assets/ccf0c3a0-3749-40e7-a149-6c74ba2ceda3" />

Cluster Name:

<img width="134" height="37" alt="image" src="https://github.com/user-attachments/assets/2583563c-29a5-414a-bf41-1e16ac16f5f7" />

Click:

<img width="121" height="32" alt="image" src="https://github.com/user-attachments/assets/de46c4b6-4719-420b-88c9-243fb535eebb" />

4. Go to **Database Access.**
5. Create a database user.

After cluster creation Atlas shows:

<img width="132" height="29" alt="image" src="https://github.com/user-attachments/assets/d7179820-1db1-4e2c-9cbb-d8933f680c85" />

Click:

<img width="97" height="32" alt="image" src="https://github.com/user-attachments/assets/ce74c45e-56ca-4edb-800b-919616c74955" />

Example:

<img width="88" height="34" alt="image" src="https://github.com/user-attachments/assets/131d4c9b-5964-4914-8e21-6c7741474144" />

Password:

<img width="115" height="33" alt="image" src="https://github.com/user-attachments/assets/0d013418-9cc2-4b41-9953-2492fcfe604f" />

(or your own)

Click:

<img width="107" height="34" alt="image" src="https://github.com/user-attachments/assets/b45c0bd2-da08-4205-9069-8b61a737f23f" />


6. Go to **Network Access.**

Atlas asks:

<img width="214" height="35" alt="image" src="https://github.com/user-attachments/assets/4bf63b78-f891-4a13-a425-cd3780f98204" />

Select:

<img width="140" height="26" alt="image" src="https://github.com/user-attachments/assets/a2ced1eb-291b-4630-860f-3e58d52463e9" />

Click:

<img width="139" height="29" alt="image" src="https://github.com/user-attachments/assets/4c730fce-13f0-47d0-9fb2-87732d6ed994" />

For testing you may use:

<img width="94" height="31" alt="image" src="https://github.com/user-attachments/assets/6393cba6-aee1-443c-8295-52a1ce985584" />

Click:

<img width="125" height="31" alt="image" src="https://github.com/user-attachments/assets/9fbf0ad6-5391-4982-80d7-7e1d547f7a19" />

7. Add your IP address, or temporarily use:

<img width="134" height="41" alt="image" src="https://github.com/user-attachments/assets/3a42d1f3-cace-4691-ab5b-cb194e046992" />

8. Go to **Database → Connect → Drivers.**
9. Copy your MongoDB connection string.

Left Menu:

<img width="90" height="36" alt="image" src="https://github.com/user-attachments/assets/bcf549bd-0ead-4f60-b7c0-7fd8b2dc0954" />

Click your cluster.

Click:

<img width="81" height="21" alt="image" src="https://github.com/user-attachments/assets/bef66d64-4be3-4776-9eed-a97ee6276e94" />

Select:

<img width="94" height="27" alt="image" src="https://github.com/user-attachments/assets/2772cfbd-c758-472c-ba2d-91a6d4bac6ed" />

Select:

<img width="100" height="25" alt="image" src="https://github.com/user-attachments/assets/a6ff03be-43b8-4bc5-b190-cacbd2ed3277" />

Copy:

mongodb+srv://username:password@cluster.mongodb.net/

Your uploaded files already contain a connection string here:

<img width="351" height="83" alt="image" src="https://github.com/user-attachments/assets/eeacec9d-4e5e-4518-ad93-2ffe030c1e56" />


10. Database name used by your code:

<img width="180" height="38" alt="image" src="https://github.com/user-attachments/assets/d59febce-683f-443e-bc29-02c156e298e7" />

11. Collection name used by your code:

<img width="157" height="36" alt="image" src="https://github.com/user-attachments/assets/0e69e433-c4b8-444c-bb25-64d6f44fdf9a" />

Open:

<img width="78" height="25" alt="image" src="https://github.com/user-attachments/assets/aad27d2e-fda3-442f-8d8b-01beeb538f4c" />

CLick:

<img width="121" height="33" alt="image" src="https://github.com/user-attachments/assets/3f8531f4-29b7-4251-bae9-21aa937ce9ab" />

Database Name:

<img width="79" height="25" alt="image" src="https://github.com/user-attachments/assets/d17550fa-5c85-4e1d-9275-6be341dbffde" />

Collection Name:

<img width="90" height="23" alt="image" src="https://github.com/user-attachments/assets/8fc34a1f-f82e-4717-979c-8c684af0d926" />

These names come directly from your code.

Click:

<img width="82" height="23" alt="image" src="https://github.com/user-attachments/assets/8a4cb5ac-4d61-4572-957f-93b11db6971e" />






