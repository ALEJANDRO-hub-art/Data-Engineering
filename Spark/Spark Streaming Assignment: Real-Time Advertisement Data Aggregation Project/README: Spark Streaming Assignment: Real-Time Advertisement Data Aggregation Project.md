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

----------------------------------------------------------------------------------------------------------------

It is one project: **Kafka → Spark Streaming → Cassandra**. The PDF says the goal is to process real-time advertisement data, aggregate by ad_id, and store/update results in Cassandra.

Files you uploaded:
- Spark Assignment.pdf. Assignment instructions.

**producer.py**
- Sends advertisement records to Kafka using Avro serialization.
 
**consumer.py**
- Test consumer that reads Avro messages from Kafka.

**stream_ads.py**
- Spark Streaming job that reads Kafka Avro data and prints it to console.

Important correction. Your assignment says the topic must be:
- ads_data

But all Python files use: **topic = "ad_topic"**

Change it to: **topic = "ads_data"**

in:
- producer.py
- consumer.py
- stream_ads.py

Where to upload/save the files. Create one project folder on Windows:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 5\2 Assignment & Solution DONE\Spark_Streaming_Solution

Put these files inside:

<img width="600" height="213" alt="image" src="https://github.com/user-attachments/assets/65adf76b-01a8-4060-85b4-7f2a92b300f2" />

Your .env file should contain:

<img width="359" height="95" alt="image" src="https://github.com/user-attachments/assets/6aa3b4dd-777e-4c3c-b30a-31504b93975b" />

Im missing: 
- mock_data.csv
- mock_data_schema.json
- .env

I generated them and pasted in the project folder:

<img width="703" height="246" alt="image" src="https://github.com/user-attachments/assets/832e6229-99f2-4e48-99aa-695d1f470ffa" />

**GUI steps: Confluent Cloud**

Create Kafka cluster

Open Confluent Cloud.

Click Environments. Open your environment or create one.

Click Create cluster.
- Choose Basic.

Select cloud/region.

Click Launch cluster.

*Lets explain it in detail:*

Open Confluent Cloud. Open your web browser.
- Go to https://confluent.cloud

Click Sign In. Log in with your Confluent account credentials.

If you do not have an account: Click Sign Up. Complete the registration process. Verify your email address.

Open Environments. After logging in:

Look at the upper-left corner of the screen. You will see the currently selected environment name (for example, Default). Click the environment drop-down.

You have two options:
- Use an Existing Environment. Select the environment you want to use.
- Create a New Environment. Click Create environment.

Enter:
<img width="499" height="75" alt="image" src="https://github.com/user-attachments/assets/e17f7641-42b7-44fd-b184-70e19e0faf5c" />

Click Create. The new environment opens automatically.

*Create the Kafka Cluster*

Inside the selected environment: Locate the Clusters section. You can access it by either:

Clicking Clusters in the left navigation menu, or Clicking the large  Create cluster button in the center of the dashboard.
- Click Create cluster.

Choose the Cluster Type. You will see several cluster options:
- Basic
- Standard
- Enterprise
- Dedicated

For course projects:
- Click the Basic tile. Click Begin configuration.

*Configure the Cluster*

Fill in the following settings:
- Cluster Name. Example:
 - orders-cluster or
 - kafka-lab

Cloud Provider. Choose one:
- AWS
- Google Cloud
- Azure

For most tutorials: Select:
- AWS
- Region

Choose the region closest to you. Since you're in Miami, common choices are:
- US East (N. Virginia) or
- US East (Ohio)
 
*Review the Estimated Cost*

For the Basic cluster page, verify:

<img width="600" height="249" alt="image" src="https://github.com/user-attachments/assets/c18367af-681b-40d1-8053-34ebc8531b37" />

Review the pricing information shown on the right side.

*Launch the Cluster*

Click the blue Launch cluster button located in the bottom-right corner. Confluent Cloud will now provision the Kafka cluster.

*Wait for Provisioning*

- You will see a status similar to: Provisioning...
- Wait approximately: 2–5 minutes
- When complete, the status changes to: Ready

What You Should See. After creation, the screen should look similar to:

<img width="375" height="192" alt="image" src="https://github.com/user-attachments/assets/98403f57-ff19-43be-a9d9-e4e0e9f61424" />










