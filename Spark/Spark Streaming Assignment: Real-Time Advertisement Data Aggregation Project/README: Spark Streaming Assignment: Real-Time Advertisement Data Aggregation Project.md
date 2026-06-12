I have the following project Spark Streaming Assignment: Real-Time Advertisement Data Aggregation Project.

<img width="868" height="213" alt="image" src="https://github.com/user-attachments/assets/64aabc84-4302-4d0b-8245-d6e0233fbaa6" />

<img width="703" height="192" alt="image" src="https://github.com/user-attachments/assets/6d12b3da-74b6-4afa-beda-4e92c32f1ec2" />

Objective: Process real-time advertisement data using Spark Streaming to gain business insights and store the aggregated data into Cassandra.

Background:
You have been provided with a Kafka topic named **ads_data** that contains advertisement data in the following format:

<img width="454" height="215" alt="image" src="https://github.com/user-attachments/assets/32ee2898-da2b-437d-82c3-13215081cb0e" />

The goal is to process this real-time data, compute business insights using window-based aggregation, and write the aggregated results into a Cassandra table. The aggregation key is ad_id, and aggregated values should update previous values in the Cassandra Table.

**Tasks:**

Kafka setup and Mock data producer:
- Set up Confluent Kafka on cloud or local
- Create topic named as **ads_data**
- Write a python script which will use above mentioned data format and keep on publishing random mock data in avro serialized form
into Kafka topic

Reading Data from Kafka:
- Set up a Spark Streaming application.
- Use the Kafka connector to read data from the **ads_data** topic.
- Parse & desearialize the incoming data into the appropriate structure.

Windowing Based Aggregation:
- Perform a window-based aggregation over a window duration (e.g., 1 minute) and sliding interval (e.g., 30 seconds).
- Aggregate the following:
  - Total clicks per ad_id.
  - Total views per ad_id.
  - Average cost per view for each ad_id.

Write Aggregated Data to Cassandra:
- For each ad_id, check if an entry already exists in the Cassandra table.
- If an entry exists, update the values:
  - Add new clicks/views to the existing counts.
  - Update the average cost per view.
- If an entry doesn't exist, create a new row with the aggregated values.

**Submission:**
Submit your Spark Streaming application code, along with a brief report detailing the results and any challenges faced during the assignment.



