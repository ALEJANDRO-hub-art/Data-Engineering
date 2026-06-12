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

**Create topic**

Open your Kafka cluster. Left menu → Topics. Click Create topic.
- Topic name: ads_data
- Partitions: 1

Click Create with defaults.

Lets explain it in detail.

Based on your uploaded files, the Python producer, consumer, and Spark scripts all use the topic name:
- topic = "ad_topic"

Specifically:
- Producer: topic = 'ad_topic'
- Spark Streaming: topic = "ad_topic"
- Consumer: topic = 'ad_topic'

Therefore, do NOT create ads_data. The correct topic name is:
- ad_topic


*Open Your Kafka Cluster*

Go to https://confluent.cloud. Sign in. Select your environment.
- Click your cluster (for example, orders-cluster).

You will arrive at the cluster overview page.

*Open Topics*

On the left navigation menu: Click: **Topics**

You should see a screen similar to:

<img width="329" height="139" alt="image" src="https://github.com/user-attachments/assets/c16893d8-e1e8-4092-94eb-ce06f07cb497" />

*Create Topic*

Click the blue button: Create topic

located near the upper-right corner.

*Configure the Topic*

Fill in the following values.

Topic Name. Enter:
- ad_topic
- 
Number of Partitions.

Set:
- 1
- 
Replication Factor. For a Basic cluster, this is automatically managed by Confluent Cloud.
- Leave the default value.

Storage Retention
- Leave the default settings.

Cleanup Policy. Leave:
- Delete (default)

*Review*

Your screen should show something similar to:

<img width="494" height="241" alt="image" src="https://github.com/user-attachments/assets/aff92549-ac2f-4a17-b779-f30d6805cce8" />

Create the Topic

Click: Create with defaults. located at the bottom-right.

*Verify the Topic*

After a few seconds, you should see:

Topics
- ad_topic
- Partitions: 1
- Messages: 0
- Status: Active

**Create API key**

Open cluster. Left menu → API keys.
- Click Create key.
- Select Global access or cluster access.

Copy:
- API key
- API secret

Put them in .env.

Lets explain this in detail.

Open Your Kafka Cluster. After logging in:
- Click Environments from the top navigation. Select the environment containing your project.
- 
Under Clusters, click your Kafka cluster. It will usually look similar to:

<img width="259" height="57" alt="image" src="https://github.com/user-attachments/assets/6b3c300f-646a-4c28-8688-ce108c4b1cdd" />

Example:

<img width="219" height="53" alt="image" src="https://github.com/user-attachments/assets/dd51fb75-5d4e-4db3-94e3-73abfe270772" />

*Open API Keys*

Inside the cluster page: Look at the left menu.
- Click: API keys

The menu path is:

<img width="355" height="125" alt="image" src="https://github.com/user-attachments/assets/7a997d16-4863-4c67-b148-ee0ebf62ef8f" />

*Create the Kafka API Key*

Click the blue button: Create key. A wizard opens.

*Choose Access Type*

You'll see two options:

Option A (Recommended). Select:
- Global access

Then click: Next

Option B. If instructed by the course:

Select: Cluster access. Choose your cluster.
- Click: Next

*Choose Permissions*

If using Cluster Access: Select:
- Developer ReadWrite or
- CloudClusterAdmin. (depending on course instructions)

Click: Continue

*Generate the Key*

Click: Create API key

Confluent now displays:
- API Key
- API Secret

For example:
- API Key: ABCD123XYZ
- API Secret: xxxxx-yyyyy-zzzzz

*Copy Them Immediately*

⚠️ Important: The secret is only shown once. Copy both values. Paste them somewhere safe.

*Update Your .env File*

Open your .env file:
- confluent_kafka_id=**YOUR_KAFKA_API_KEY**
- confluent_kafka_secret_key=**YOUR_KAFKA_API_SECRET**
- confluence_schema_id=YOUR_SCHEMA_REGISTRY_KEY
- confluence_schema_secret=YOUR_SCHEMA_REGISTRY_SECRET

Replace:
- confluent_kafka_id=**ABCD123XYZ**
- confluent_kafka_secret_key=**xxxxxxxx**

with the values you copied.

**Create Schema Registry API key**

Left menu → Schema Registry. Enable Schema Registry if needed.

Go to API keys.
- Click Create key. Copy key and secret.

Put them in .env.

Lets explain this in detail.

*Select the Correct Environment*

From the top navigation bar:Environments
- Click the environment containing your Kafka cluster. Example:default
- 
*Open Schema Registry*

On the left-hand menu, click: Schema Registry

The navigation path looks like:

<img width="328" height="110" alt="image" src="https://github.com/user-attachments/assets/873a11d8-fa04-46e3-8056-838931e8c387" />

*Enable Schema Registry (If Required)*

If this is your first time opening Schema Registry, you'll see a page similar to: Schema Registry is not enabled.
- Click: Enable Schema Registry

Wait a few moments while Confluent provisions it. Once enabled, you'll see the Schema Registry dashboard.

*Open Schema Registry API Keys*

Inside Schema Registry:
- Click: API Keys

You should see a page similar to:

<img width="390" height="93" alt="image" src="https://github.com/user-attachments/assets/c54e7775-ba42-486d-a86f-996f4acc9cce" />

*Create the Schema Registry API Key*

Click the blue button: Create key. A wizard will appear.

*Select the Schema Registry Cluster*

If prompted: Select the available Schema Registry cluster. 
- Click: Next

Usually there is only one option.

Generate the Credentials*
- Click: Create API key

Confluent will display:
- API Key
- API Secret

For example:
- API Key: SR123ABC456
- API Secret: xxxxxxxxxxxxxxxx

*Copy Both Values Immediately*

⚠️ The secret is shown only once. Copy:
- Schema Registry API Key
- Schema Registry API Secret

Save them somewhere safe.

*Update the .env File*

Open your .env file and replace the placeholders:
- confluent_kafka_id=YOUR_KAFKA_API_KEY
- confluent_kafka_secret_key=YOUR_KAFKA_API_SECRET
- confluence_schema_id=**YOUR_SCHEMA_REGISTRY_KEY**
- confluence_schema_secret=**YOUR_SCHEMA_REGISTRY_SECRET**

with your actual values.

For example:
- confluent_kafka_id=ABCD123XYZ
- confluent_kafka_secret_key=kafka-secret-here
- confluence_schema_id=**SR123ABC456**
- confluence_schema_secret=**schema-secret-here**

*How These Credentials Are Used in Your Project*
- **producer.py** uses the Schema Registry credentials to serialize Avro messages before publishing them to Kafka.
- **stream_ads.py** uses them to retrieve the latest schema and decode Kafka records inside Spark Structured Streaming.
- **consumer.py** uses them to deserialize Avro messages consumed from Kafka.

**Create Avro schema**

Use this schema for topic value:

<img width="483" height="248" alt="image" src="https://github.com/user-attachments/assets/b4adeeca-ab6f-4241-8299-3db7bfac6753" />

Subject name should be:
- ads_data-value

Lets explain this in detail.

*Select Your Environment*

From the top navigation: Click: Environments. Then select the environment containing your Kafka cluster.
- Example: default

**Open Schema Registry**

From the left menu, click: Schema Registry

The navigation path looks like:

<img width="366" height="111" alt="image" src="https://github.com/user-attachments/assets/d456a023-f52f-4175-83b3-025f97906abb" />

*Open Schemas*

Inside Schema Registry: Click: Schemas

You'll see either:
- No schemas found or a list of existing schemas.

*Click "Add Schema"*

Click the blue button: + Add schema. A form will open.

*Select the Subject Name*

Under: Subject name
- enter: ads_data-value

according to your assignment instructions.

However, your uploaded Python files actually expect:

<img width="340" height="92" alt="image" src="https://github.com/user-attachments/assets/17a441d6-3a96-4806-b393-b669d6a72913" />

which means the subject should be:
- ad_topic-value

because all three scripts retrieve:

<img width="285" height="64" alt="image" src="https://github.com/user-attachments/assets/37c7903a-f768-416b-9714-a4f091e156ba" />

from Schema Registry.

Therefore: Use:
- ad_topic-value

unless you also change the topic names inside the Python scripts.

*Select Schema Type*

Under: Schema format
- choose: Avro

from the dropdown.

*Paste the Schema*

Delete any example text.

Paste:

<img width="375" height="515" alt="image" src="https://github.com/user-attachments/assets/d8f356f7-f18d-4a6d-bb53-e4994b4d7581" />








