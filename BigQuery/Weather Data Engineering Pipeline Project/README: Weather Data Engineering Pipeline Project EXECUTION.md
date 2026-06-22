I have this project Weather Data Engineering Pipeline Project.

<img width="677" height="292" alt="image" src="https://github.com/user-attachments/assets/99f464af-ca0c-4704-a070-eb56fe12cb78" />

<img width="565" height="191" alt="image" src="https://github.com/user-attachments/assets/6381975e-217c-4bd9-b849-dfd243080326" />

<img width="625" height="190" alt="image" src="https://github.com/user-attachments/assets/41fff38c-1ced-4000-ae5c-fdb8cfb3cec8" />

<img width="638" height="191" alt="image" src="https://github.com/user-attachments/assets/cd64115d-5a76-4df5-8ffa-608203d6e087" />

<img width="626" height="197" alt="image" src="https://github.com/user-attachments/assets/a7568829-bbdb-42a9-b681-2ce615a50b9d" />

<img width="720" height="187" alt="image" src="https://github.com/user-attachments/assets/9ff951b2-5638-4167-9c73-9d4a0627a8cf" />

<img width="638" height="237" alt="image" src="https://github.com/user-attachments/assets/9e6e7e4a-2a25-43da-9e0a-5f3fbd4f4d44" />

<img width="657" height="257" alt="image" src="https://github.com/user-attachments/assets/b6255f5e-9023-455e-94a4-469c7d2faeb6" />

<img width="637" height="254" alt="image" src="https://github.com/user-attachments/assets/a7d6dd57-40a7-49d3-a950-c2aa4bba6fea" />

<img width="661" height="378" alt="image" src="https://github.com/user-attachments/assets/2989b1a5-1090-4b73-9275-a4ac26841cf7" />

<img width="678" height="410" alt="image" src="https://github.com/user-attachments/assets/157bfe06-a01b-4a48-822e-b3e2ff537f2e" />

<img width="657" height="150" alt="image" src="https://github.com/user-attachments/assets/a3e06fd6-ef27-45df-a5a8-9a3a4469313c" />

<img width="670" height="168" alt="image" src="https://github.com/user-attachments/assets/240cd3e4-1574-4709-9183-8f2dd068c822" />

<img width="724" height="168" alt="image" src="https://github.com/user-attachments/assets/5ae03932-af2b-4e5f-94b2-3183860bd235" />

<img width="668" height="167" alt="image" src="https://github.com/user-attachments/assets/b2a45ef7-4ddb-4efa-ad11-061ad4eb05e7" />

<img width="691" height="160" alt="image" src="https://github.com/user-attachments/assets/40fffa49-a5a1-4972-bf24-4aa0e6857a0e" />

<img width="735" height="190" alt="image" src="https://github.com/user-attachments/assets/25d2ba0c-6401-4d07-b7c9-bf5a6c514eef" />

<img width="687" height="502" alt="image" src="https://github.com/user-attachments/assets/7e94ed92-5152-4f19-abe4-13d8c1fde766" />

<img width="673" height="193" alt="image" src="https://github.com/user-attachments/assets/06d49309-5054-40fd-ace9-dcbec011ee81" />

<img width="709" height="168" alt="image" src="https://github.com/user-attachments/assets/61994b50-b11b-403c-9879-a00ee0b50e07" />

<img width="714" height="156" alt="image" src="https://github.com/user-attachments/assets/cc04522b-ce1c-4c65-8502-193577e2cab0" />

<img width="690" height="190" alt="image" src="https://github.com/user-attachments/assets/1b093217-86c4-4648-8588-ed5888b8fe97" />

<img width="703" height="158" alt="image" src="https://github.com/user-attachments/assets/90500496-4066-4f98-89d2-a07b4493909d" />

<img width="645" height="152" alt="image" src="https://github.com/user-attachments/assets/e1bf4748-8a22-4d8c-b0c0-d6059f52a1b1" />

<img width="713" height="157" alt="image" src="https://github.com/user-attachments/assets/8f2e154b-b57a-4270-a326-c325baea33f2" />

<img width="646" height="146" alt="image" src="https://github.com/user-attachments/assets/67c68778-1da2-4daa-a0b8-11668528048e" />

<img width="701" height="167" alt="image" src="https://github.com/user-attachments/assets/57859426-05b4-49c1-bd76-ece7cbe7b22b" />

<img width="777" height="360" alt="image" src="https://github.com/user-attachments/assets/078cf0c9-48b6-472a-82ef-8dd99e8069a2" />

<img width="233" height="78" alt="image" src="https://github.com/user-attachments/assets/6967039e-4244-47c9-b3f3-87b50bcc628f" />


BigQuery / GCP data engineering learning portfolio with multiple small pipelines. The uploaded document explains that the folders cover managed BigQuery tables, external tables, Pub/Sub streaming, medallion architecture, and a weather pipeline with Airflow/Dataproc/BigQuery.


**End-to-end architecture**

<img width="470" height="283" alt="image" src="https://github.com/user-attachments/assets/37b6e153-e211-4c3f-b179-5917748fd9d1" />

**File explanation and where to upload each file**

*A. Managed Tables in BigQuery*

<img width="618" height="216" alt="image" src="https://github.com/user-attachments/assets/724cc147-3f93-4e0d-97d4-59beb168994b" />

Purpose: This project creates a native BigQuery managed table from a CSV file. The data is physically stored inside BigQuery.

Workflow:

<img width="337" height="157" alt="image" src="https://github.com/user-attachments/assets/cffd3fe8-9ef8-415d-a3a1-e1bb2afc7376" />

*B. External Tables in BigQuery*

<img width="623" height="179" alt="image" src="https://github.com/user-attachments/assets/74646410-a854-46fb-8c5f-fd389a0cd7fa" />

The uploaded JSON files contain ride records such as ride_id, user_id, driver_id, locations, timestamps, distance, and price.

Purpose: This project creates a BigQuery table that does not store the data inside BigQuery. Instead, BigQuery reads the JSON directly from GCS.

Workflow:

<img width="345" height="126" alt="image" src="https://github.com/user-attachments/assets/c4810aaa-4499-45ee-b803-c6d323d7dcc2" />

*C. Starbucks Data Canvas Dataset*

<img width="590" height="153" alt="image" src="https://github.com/user-attachments/assets/8705b1d8-4a8e-4663-9d10-5f1229a610f4" />

Purpose: This is an analytics dataset. You use it to analyze customer behavior, offers, transactions, and segmentation.

Workflow:

<img width="364" height="122" alt="image" src="https://github.com/user-attachments/assets/ce7faf58-a86a-4e76-9631-a77e9516520b" />

*D. Loyalty Program Pub/Sub Streaming Pipeline*

<img width="619" height="195" alt="image" src="https://github.com/user-attachments/assets/7632d938-51ed-41b2-8692-c35096549244" />

mock_data_to_pubsub.py publishes mock customer fields like name, age, email, join date, loyalty points, account balance, and timestamps to a Pub/Sub topic.

transform_udf.py formats names, lowercases emails, creates loyalty_status, fixes timestamps, and calculates account_age_days.

Purpose: This simulates a real-time streaming pipeline.

Workflow:

<img width="319" height="152" alt="image" src="https://github.com/user-attachments/assets/42dc051f-c6f6-46a0-aa89-e7a3887e1694" />

*E. Telecom Medallion Pipeline*

<img width="645" height="157" alt="image" src="https://github.com/user-attachments/assets/91e9c347-f43d-4355-8ce1-d180d0eb8d10" />

The Silver script reads the Bronze table, removes bad rows, casts dates/numbers, and writes a cleaned Silver table partitioned by call_date and clustered by region and plan_type.

The Gold script reads the Silver table and creates KPI metrics like total calls, average duration, total duration, average data usage, and total data usage by date, region, and plan.

Purpose: This project teaches Medallion Architecture:

<img width="279" height="92" alt="image" src="https://github.com/user-attachments/assets/9aca5ee9-019d-4d33-906a-cad01fe562e5" />

*F. Weather Data Processing Pipeline*

<img width="638" height="292" alt="image" src="https://github.com/user-attachments/assets/b2d7a903-5735-45f9-be8e-12fc5bcdeecb" />

extract_data_dag.py calls OpenWeather, normalizes the JSON with pandas, uploads forecast.csv to GCS, and triggers the downstream transform DAG.

transform_data_dag.py submits a Dataproc Serverless PySpark batch job using weather_data_processing.py.
weather_data_processing.py reads the weather CSV from GCS, casts fields, renames columns, and writes the processed result to BigQuery.

Workflow:

<img width="304" height="194" alt="image" src="https://github.com/user-attachments/assets/3691fc24-6a86-41b6-8046-0ca132ae8980" />

**Step-by-step GUI execution**

**Step 1 — Create GCS buckets**

Go to: **Google Cloud Console → Cloud Storage → Buckets → Create**

Create buckets such as:
- **bigquery-data-gds**
- **weather-data-gds**
- **bq-temp-gds**

**Upload files to GCS**

GUI path: **Cloud Storage → Buckets → your bucket → Upload files**

Upload:
- **telecom_data.csv** → bigquery-data-gds/telecom/
- **lyft JSON files** → bigquery-data-gds/raw/date=2024-08-08/
- **weather_data_processing.py** → weather-data-gds/script/

**Run BigQuery SQL files**

Go to: **BigQuery → SQL Workspace → New Query**

Run these files one by one:
- **commands.sql**
- **scheduled_query.sql**
- **create_bq_external_table.sql**
- **bigquery_create_table.sql**

Use them to create:
- telecom_db
- lyft_db
- loyalty destination table
- forecast dataset/table

**Create Pub/Sub topic**

Go to: **Pub/Sub → Topics → Create Topic**

Create topic: **loyality_data**

Then run: **mock_data_to_pubsub.py**

This sends fake loyalty records into Pub/Sub.

Lets explain this in detail.

*Exact GUI Steps — Step 4: Create Pub/Sub Topic*

*1. Open Google Cloud Console*

Go to: https://console.cloud.google.com

Make sure you are in the correct project: mythic-aloe-457912-d5

You can verify this from the project selector at the top of the page.

*2. Open Pub/Sub*

In the top search bar type: Pub/Sub
- Click: Pub/Sub

or navigate through:

☰ Navigation Menu
   → Analytics
      → Pub/Sub

*3. Open Topics*

In the left menu click: Topics

You should see a screen similar to:

Pub/Sub
- ├─ Topics
- ├─ Subscriptions
- ├─ Schemas
- └─ Snapshots

*4. Create Topic*

Click the blue button: + CREATE TOPIC. Located near the top of the page.

*5. Fill Topic Information*

In the Topic ID field enter: loyality_data

⚠️ Important:

Your Python file contains:
- topic_id = "loyality_data"

Notice it is spelled: loyality_data NOT loyalty_data

The topic name must exactly match the Python code.

*6. Leave Defaults*

Leave everything else as default:

Encryption
- ✓ Google-managed key

Message retention
- ✓ Default

Schema
- ✓ None

Storage policy
- ✓ Default

No changes needed.

*7. Click Create*

Click: CREATE

Google creates: projects/mythic-aloe-457912-d5/topics/loyality_data

*8. Verify Topic Creation*

You should now see:

Topic Name
--------------------------------
loyality_data

Click the topic. You will see: Topic Details. with:
- Topic ID: loyality_data

*Optional: Create Subscription (Good for Testing)*

While not required for Dataflow, you can create a subscription to see messages arriving.

Inside the topic page click: CREATE SUBSCRIPTION

Fill:
- Subscription ID: loyality_data-sub
- Delivery Type: Pull
- Expiration: Never Expire

Click: CREATE

*9. Run the Python Generator*

After the topic exists, run: **python mock_data_to_pubsub.py**

The script will:

Generate 20 fake customer records
↓
Publish them to Pub/Sub
↓
Print message IDs

as defined in the file.

Expected Architecture After This Step
**mock_data_to_pubsub.py**
         ↓
     Pub/Sub Topic
     loyality_data
         ↓
   (next step)
      Dataflow
         ↓
     BigQuery

The next GUI step after this is creating the Dataflow streaming job that reads from loyality_data and uses transform_udf.py to write clean records into BigQuery.



























**Create Dataflow streaming job**

Go to: **Dataflow → Create Job from Template**

Choose a Pub/Sub-to-BigQuery streaming template if your course uses template-based execution.

Use:
- Input Pub/Sub topic: **loyality_data**
- Output BigQuery table: your loyalty table
- UDF path: **gs://your-bucket/transform_udf.py**

Lets explain this in detail.





















