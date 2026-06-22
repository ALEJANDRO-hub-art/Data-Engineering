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

**mock_data_to_pubsub.py** publishes mock customer fields like name, age, email, join date, loyalty points, account balance, and timestamps to a Pub/Sub topic.

**transform_udf.py** formats names, lowercases emails, creates loyalty_status, fixes timestamps, and calculates account_age_days.

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

**extract_data_dag.py** calls OpenWeather, normalizes the JSON with pandas, uploads forecast.csv to GCS, and triggers the downstream transform DAG.

**transform_data_dag.py** submits a Dataproc Serverless PySpark batch job using weather_data_processing.py.
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

Make sure you are in the correct project: **mythic-aloe-457912-d5**

You can verify this from the project selector at the top of the page.

*2. Open Pub/Sub*

In the top search bar type: Pub/Sub
- Click: Pub/Sub

or navigate through:

☰ Navigation Menu ➜ Analytics ➜ Pub/Sub

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

In the Topic ID field enter: **loyality_data**

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

Google creates: **projects/mythic-aloe-457912-d5/topics/loyality_data**

*8. Verify Topic Creation*

You should now see:

**Topic Name**
--------------------------------
`loyality_data`

Click the topic. You will see: Topic Details. with:
- Topic ID: **loyality_data**

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
- Generate 20 fake customer records ➜ Publish them to Pub/Sub ➜ Print message IDs

as defined in the file.

Expected Architecture After This Step

**mock_data_to_pubsub.py** ➜ **Pub/Sub Topic loyality_data ➜ (next step) Dataflow ➜ BigQuery**

The next GUI step after this is creating the Dataflow streaming job that reads from **loyality_data** and uses **transform_udf.py** to write clean records into BigQuery.

**Create Dataflow streaming job**

Go to: **Dataflow → Create Job from Template**

Choose a Pub/Sub-to-BigQuery streaming template if your course uses template-based execution.

Use:
- Input Pub/Sub topic: **loyality_data**
- Output BigQuery table: your loyalty table
- UDF path: **gs://your-bucket/transform_udf.py**

Lets explain this in detail.

**Exact GUI Steps**

**Step 5: Create Dataflow Streaming Job**

This step creates the streaming pipeline:

**Pub/Sub Topic (loyality_data) ➜ Dataflow ➜ transform_udf.py ➜ BigQuery**

*Step 5.1 — Create BigQuery Destination Table First*

Before Dataflow can write data, create the destination table.

Go to: BigQuery. Open: SQL Workspace. Click: + New Query
- Paste and run: **bigquery_create_table.sql**

After execution verify you have:
- Dataset: loyalty_db
- Table: customer_loyalty

(or whatever table name exists in your SQL file).

*Step 5.2 — Upload transform_udf.py to Cloud Storage*

Go to: Cloud Storage. Open your bucket. Example: **bigquery-data-gds**
- Create folder: udf/
- Click: Upload Files. Upload: **transform_udf.py**

Final path should look like:
- **gs://bigquery-data-gds/udf/transform_udf.py**
 
*Step 5.3 — Open Dataflow*

Go to:
- ☰ Navigation Menu ➜ Dataflow or search: Dataflow

*Step 5.4 — Create Job*

Click: CREATE JOB FROM TEMPLATE. You will see: Create Dataflow Job

*Step 5.5 — Select Region*

Region: us-central1 (Use the same region as Pub/Sub and BigQuery.)

*Step 5.6 — Choose Template*

Under: Dataflow Template. Choose: Pub/Sub Subscription to BigQuery or Pub/Sub to BigQuery

(depending on your Dataflow version)

Click: NEXT

*Step 5.7 — Fill Job Information*

Job Name: **loyalty-streaming-job**

Streaming Mode: Streaming

*Step 5.8 — Create Subscription*

Dataflow usually reads from a subscription, not directly from the topic.

Go back to Pub/Sub. Open: Topics
- Click: **loyality_data**
- Click: CREATE SUBSCRIPTION

Fill:
- Subscription ID: loyality_data-sub
- Delivery Type: Pull

Click: CREATE

*Step 5.9 — Fill Dataflow Source*

Back in Dataflow.

For Input Subscription select: **projects/mythic-aloe-457912-d5/subscriptions/loyality_data-sub**

*Step 5.10 — Fill BigQuery Destination*

Destination Table: **mythic-aloe-457912-d5:loyalty_db.customer_loyalty**

Replace with your actual dataset/table name if different.

*Step 5.11 — Temporary Files Location*

Create bucket folder: **gs://bigquery-data-gds/temp**

Enter: **gs://bigquery-data-gds/temp**. for: Temporary Location

*Step 5.12 — Service Account*

Leave default: Compute Engine Default Service Account or: PROJECT_NUMBER-compute@developer.gserviceaccount.com

*Step 5.13 — Launch Job*

Click: RUN JOB. 

Dataflow will begin provisioning workers.

Wait until status becomes: Running

*Step 5.14 — Generate Test Data*

Now run: **python mock_data_to_pubsub.py**

The script publishes 20 records to: **loyality_data** topic.

*Step 5.15 — Verify Messages*

Go to:
- **Pub/Sub ➜ Subscriptions ➜ loyality_data-sub**

You should see: Unacknowledged messages

changing as Dataflow consumes them.

*Step 5.16 — Verify BigQuery*

Go to: BigQuery
- Open: **loyalty_db**
- Open: **customer_loyalty**

Click: Preview

You should see rows arriving.

The rows will contain fields such as:
- row_key
- name
- email
- age
- join_date
- loyalty_points
- account_balance
- loyalty_status
- account_age_days
- inserted_at
- updated_at

which are created by **mock_data_to_pubsub.py** and enriched by **transform_udf.py.**

Expected Final Architecture

**mock_data_to_pubsub.py** ➜ Pub/Sub Topic **loyality_data** ➜ Subscription **loyality_data-sub** ➜ Dataflow ➜ **transform_udf.py** ➜ BigQuery Table **customer_loyalty**

**Run Telecom Silver and Gold scripts**

Run in this order:
- 1 **telecom_calls_silver_layer.py**
- 2 **telecom_calls_gold.py**

The first creates the cleaned Silver table. The second creates the Gold KPI table.

**Create Cloud Composer environment**

Go to: **Composer → Environments → Create**

Use:
- Name: weather-composer
- Region: us-central1
- Composer version: Composer 3

After the environment is created, open its DAGs bucket and upload:
- **extract_data_dag.py**
- **transform_data_dag.py**

**Add Airflow variable**

Open Composer Airflow UI: **Composer → your environment → Open Airflow UI**

Then: Admin ➜ Variables ➜ +

Create:
- Key: **openweather_api_key**
- Value: **your OpenWeather API key**

Lets explain this in detail.

**Exact GUI Steps — Step 8: Add Airflow Variable**

This step stores your OpenWeather API key inside Airflow so that the DAG can read it using:

<img width="226" height="57" alt="image" src="https://github.com/user-attachments/assets/f1242092-6889-46d6-b65b-e4ebd4f67aa9" />

as shown in **extract_data_dag.py.**

*1. Open Cloud Composer*

Go to: **https://console.cloud.google.com**

In the search bar type: Composer. Click: Cloud Composer

*2. Open Your Composer Environment*

You should see something similar to:

<img width="228" height="72" alt="image" src="https://github.com/user-attachments/assets/ca5230a0-ac9b-4d9f-a934-ddecc9967dfa" />

or whatever name you gave your environment.

Click the environment name. Example: **weather-composer**

*3. Open Airflow UI*

Inside the environment page locate: Airflow web server. Click: OPEN AIRFLOW UI

A new browser tab opens.

*4. Login (if prompted)*

Sometimes Composer automatically logs you in. If prompted: Continue with Google. Select your Google Cloud account.

*5. Open Variables*

Inside Airflow look at the top menu. Click: Admin. A dropdown appears. Click: Variables

Path:
- Admin ➜ Variables

You will see a page similar to:

Variables
------------------------------------
Key             Value
------------------------------------

*6. Create New Variable*

Click the blue: + button or Add a new record ; depending on the Airflow version. Usually located in the upper-right corner.

*7. Fill Variable Information*

In the form enter:
- Key: openweather_api_key
- Value: Paste your OpenWeather API key: 123456789abcdef123456789abcdef

(Your actual key will be different.)

*8. Save*

Click: Save

You should now see:

Variables
------------------------------------
openweather_api_key    ************

*9. Verify the DAG Uses It*

Your DAG contains:

<img width="234" height="51" alt="image" src="https://github.com/user-attachments/assets/5647f8f5-fee1-42b1-b0c8-9b3541ef7170" />

which means Airflow will retrieve the value you just stored.

*10. Test the Variable*

Go to: DAGs
- Find: **openweather_api_to_gcs**

Turn it ON if it is paused.

Then click: ▶ Trigger DAG

Airflow will: **Read openweather_api_key ➜ Call OpenWeather API ➜ Create forecast.csv ➜ Upload forecast.csv to GCS ➜ Trigger transformed_weather_data_to_bq**

as defined in the DAG workflow.

What You Should See After Success

Airflow
- DAGs
-----------------------------------
- openweather_api_to_gcs        **Success**
- transformed_weather_data_to_bq **Success**

**GCS**

```text
📁 weather-data-gds
└── 📁 weather
    └── 📁 YYYY-MM-DD
        └── 📄 forecast.csv
```

**BigQuery**
```text
forecast
└── weather_data
```

with weather forecast rows loaded by the Spark job.

If you haven't created the OpenWeather API key yet, I can also give you the exact GUI steps on the OpenWeather website to create the API key. How do we create that **Value** for **openweather_api_key.**

*Exact GUI Steps — Create an OpenWeather API Key*

This API key is required because your Airflow DAG calls:

<img width="307" height="66" alt="image" src="https://github.com/user-attachments/assets/5cb57678-8af9-4d6a-8d45-73b99038c159" />

and reads the key from:

<img width="274" height="63" alt="image" src="https://github.com/user-attachments/assets/5e49150c-b38f-4dad-807a-78921db5ef04" />

*Step 1 — Open OpenWeather*

Go to: **OpenWeather**

Step 2 — Create Account

Click: Sign In (top-right corner). Then click: Create Account

*Step 3 — Fill Registration Form*

Enter:
- Username
- Email Address
- Password
- Confirm Password

Example:
- Username: alejandrov
- Email: your email
- Password: ********

Check:
- ☑ I am not a robot
- ☑ Terms and Conditions

Click: Create Account

*Step 4 — Verify Email*

Open your email inbox. Look for an email from: **OpenWeather**. Open it. Click: Verify Email or Activate Account

*Step 5 — Log In*

Return to: OpenWeather Login

Enter:
- Email
- Password

Click: Sign In

*Step 6 — Open API Keys Page*

After login click your username in the upper-right corner.

Then click: My API Keys or go directly to: My API Keys

*Step 7 — Create New API Key*

You will see something similar to:

<img width="237" height="71" alt="image" src="https://github.com/user-attachments/assets/e2faa5e9-fc42-4a9d-9495-ec790e12de7a" />

You can either:

*Option A*. Use the automatically created key.

OR

*Option B*. Create your own.
- In: Create Key. type: **weather-airflow-key**. Click: Generate

*Step 8 — Copy API Key*

You will receive something like: 9f5c3c8e1e2d4a7b8c9d0e1f2a3b4c5d. Copy the entire value.

*Step 9 — Wait for Activation*

⚠️ Very important:

New OpenWeather keys often take:
- 10 minutes to 2 hours to become active. Sometimes up to: 24 hours for free accounts.

If your DAG fails immediately after creating the key, wait a little and try again.

*Step 10 — Test the API Key in Browser*

Replace YOUR_KEY with your actual key:
- https://api.openweathermap.org/data/2.5/forecast?q=Toronto,CA&appid=YOUR_KEY

Example: https://api.openweathermap.org/data/2.5/forecast?q=Toronto,CA&appid=9f5c3c8e...

Paste into your browser.

If working, you'll see JSON like:

<img width="167" height="112" alt="image" src="https://github.com/user-attachments/assets/4df7622d-d272-43ec-9d35-1f0da271a552" />

If you get:

<img width="214" height="104" alt="image" src="https://github.com/user-attachments/assets/51125c86-1954-4339-8d6a-e56bc3c46d40" />

the key is not active yet.

*Step 11 — Add the Key to Airflow*

Open:

Composer
- → Environment
- → Open Airflow UI
- → Admin
- → Variables
- → +

Enter:
- Key **openweather_api_key**
- Value **YOUR_OPENWEATHER_KEY**

Example: 9f5c3c8e1e2d4a7b8c9d0e1f2a3b4c5d

Click: Save

*Step 12 — Trigger the DAG*

Go to:
- Airflow UI ➜ DAGs

Find: **openweather_api_to_gcs**

Click: ▶ Trigger DAG

The DAG will:

**OpenWeather API ➜ forecast data ➜ GCS weather bucket ➜ Dataproc Spark ➜ BigQuery forecast.weather_data**

Once the DAG succeeds, your weather pipeline is fully connected end-to-end.

Lets continue.

**Run weather DAG**

In Airflow UI: **DAGs ➜ openweather_api_to_gcs ➜ Trigger DAG**

This will:
- Call OpenWeather API
- Upload forecast.csv to GCS
- Trigger transformed_weather_data_to_bq
- Run Dataproc Serverless Spark
- Load final data into BigQuery

**Final project meaning**

This full project collection teaches:
- BigQuery managed tables
- BigQuery external tables
- CSV and JSON ingestion
- GCS storage
- Pub/Sub streaming
- Dataflow transformations
- Medallion architecture
- Airflow orchestration
- Dataproc Serverless Spark
- BigQuery analytics tables

The strongest final architecture is:

Sources
- CSV / JSON / API / Python Events

➜ ingestion

Google Cloud Storage / Pub/Sub

➜ processing

BigQuery SQL / Dataflow / Spark

➜ orchestration

Airflow / Composer

➜ final layer

BigQuery Silver and Gold tables

➜ output

Analytics-ready datasets and dashboards





