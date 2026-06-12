I have the following project Kafka + Spark Stateful Transaction Aggregation Project.

<img width="858" height="233" alt="image" src="https://github.com/user-attachments/assets/52b3b7e6-30fc-4019-8f33-90717c9fe552" />

**It has 2 Spark streaming jobs:**

Stateful GroupBy Aggregation
- File: **kafka_spark_stateful_groupby.py**
- Calculates total transaction amount per user.

Stateful Window GroupBy Aggregation
- File: **kafka_spark_stateful_window_groupby.py**
- Calculates total transaction amount per user every 3-minute window.

The producer sends JSON transaction data into Kafka **topic trx_topic_data.**
The dataset is **user_transactions.json.**

**Files and where to upload them**

Put all files in one local project folder on Windows:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 5\1 Class Content PPT, Notes, Exercises DONE\Stateful_GroupBy_Streaming_Pipeline DONE

<img width="707" height="167" alt="image" src="https://github.com/user-attachments/assets/28adbe59-6e72-4061-9b2e-8e41d35f40eb" />

<img width="711" height="314" alt="image" src="https://github.com/user-attachments/assets/cece4fa6-9871-4c90-a6d9-4300e90cd67f" />

**Create Kafka topic in Confluent GUI**

Go to: **Confluent Cloud → Environment → Cluster → Topics**

Create topic:
- trx_topic_data

Open Confluent Cloud. Open your browser.
- Go to https://confluent.cloud

Sign in to your Confluent Cloud account.

Open Your Environment

On the left navigation panel: Click Environments.

Click the environment that contains your Kafka cluster (for example, default).

You should now see your cluster(s).

Open the Kafka Cluster. Under Kafka Clusters, locate your cluster. Click the cluster name.

Example:

<img width="385" height="75" alt="image" src="https://github.com/user-attachments/assets/82c93119-f87b-4093-b7b2-2718a3bf39fd" />

**Upload files locally**

Put these files in:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 5\1 Class Content PPT, Notes, Exercises DONE\Stateful_GroupBy_Streaming_Pipeline DONE


**Open your Windows Command Prompt (cmd)**

Do:

cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 5\1 Class Content PPT, Notes, Exercises DONE\Stateful_GroupBy_Streaming_Pipeline DONE"

**Install producer dependency**

Run:
- pip install confluent-kafka

**Start the Kafka producer**

Run:
- python trx_data_producer.py

This sends the JSON records into Kafka topic:
- trx_topic_data

**Run Spark job 1: normal stateful groupBy**

Run this in your Spark/YARN environment:
- spark-submit kafka_spark_stateful_groupby.py

This shows total amount per user_id.

**Run Spark job 2: window groupBy**

Stop the first Spark job with:
- Ctrl + C

Then run:
- spark-submit kafka_spark_stateful_window_groupby.py

This shows totals per user_id every 3 minutes.

<img width="709" height="394" alt="image" src="https://github.com/user-attachments/assets/d4e6ce87-5706-4727-9fa8-b7332cd632ff" />














