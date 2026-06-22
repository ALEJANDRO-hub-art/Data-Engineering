I have this project News Data Analysis Project.

<img width="647" height="252" alt="image" src="https://github.com/user-attachments/assets/61f49bdd-6b02-45a5-aad4-354d63951b15" />

This is a News Data Analysis Pipeline project.

It moves data like this:

**NewsAPI → Airflow → Google Cloud Storage → Snowflake → Analytics Tables**

**What each file does**

**fetch_news.py**
Python script that calls NewsAPI, gets news articles, cleans them, converts them into a pandas DataFrame, saves them as a Parquet file, and uploads the file to GCS. It reads the API key from the Airflow Variable NEWS_API_KEY.

**news_api_airflow_job.py**
This is the Airflow DAG. It controls the full workflow: fetch news, upload to GCS, create Snowflake table, copy data into Snowflake, and create summary tables.

**snowflake_commands.sql**
Run this manually inside Snowflake. It creates the news_api database, Parquet file format, GCS storage integration, and external stage.

**README.md**
Documentation explaining the architecture, files, setup steps, and expected output tables.

**airflow_snowflake_connection.png**
Reference screenshot showing how the Snowflake connection should look in Airflow.

**Where to download/place the files**

Create this folder on your computer:
- C:\airflow-news-project

Inside it, create:
- C:\airflow-news-project\dags
- C:\airflow-news-project\logs
- C:\airflow-news-project\plugins
- C:\airflow-news-project\config

Place files like this:
- C:\airflow-news-project\dags\news_api_airflow_job.py 
- C:\airflow-news-project\dags\fetch_news.py
- C:\airflow-news-project\snowflake_commands.sql**
- C:\airflow-news-project\README.md
- C:\airflow-news-project\airflow_snowflake_connection.png
- C:\airflow-news-project\config\gcp-key.json

Do not upload snowflake_commands.sql to Airflow. You run it inside Snowflake Snowsight.

**Exact GUI execution steps**

**Step 1 — NewsAPI**

Go to NewsAPI website. Create an account. Copy your API key.

You will save it later in Airflow as:
- NEWS_API_KEY

Lets explain this in detail.

You are currently at the Snowflake Connection setup screen in Airflow. Before this connection works, you must first create and save your NewsAPI key in Airflow because fetch_news.py retrieves it using:

<img width="291" height="65" alt="image" src="https://github.com/user-attachments/assets/ceb7c1b0-0546-4caa-af31-1185d2ef0c77" />

*Create NewsAPI Account and Get API Key*

*1. Open NewsAPI*

Go to:https: //newsapi.org

*2. Create Account*

Click: Get API Key or Register

*3. Fill Registration Form*
 
<img width="463" height="302" alt="image" src="https://github.com/user-attachments/assets/5085f66c-aaf3-47b4-917b-0eb41633ca43" />

*4. Verify Email*

NewsAPI sends a verification email. Open your email.
- Click: Verify Email Address

*5. Login*

Return to: https://newsapi.org

Click: Login

Enter:
- Email
- Password

*6. Copy API Key*

After login you'll see:

Your API Key
- 4f6xxxxxxxxxxxxxxxxxxxxxxxxxxxx

Copy the entire key.

Example:
- 4f6d8c123456789abcdef123456789ab

Keep it somewhere temporarily.

*Open Airflow UI*

Open your Airflow URL.

Example: http://localhost:8080 or http://34.xx.xx.xx:8080

depending on your environment.

*Create Airflow Variable*

The project expects:

<img width="251" height="64" alt="image" src="https://github.com/user-attachments/assets/4c049ce4-c743-4eef-bc68-73b9a844d229" />

Therefore Airflow must contain a Variable named: **NEWS_API_KEY**

*Exact GUI Steps*

*Airflow Home*

Click: Admin -> Variables

You should see a page similar to:

<img width="222" height="78" alt="image" src="https://github.com/user-attachments/assets/a98f6acf-8c56-4930-afcc-ac4c0fb6bd38" />

*Click +*

Upper-right corner: + or Add Variable

*Fill Variable Form*

Key:
- NEWS_API_KEY

Value. Paste your NewsAPI key. Example:
- 4f6d8c123456789abcdef123456789ab

Description (optional)
- NewsAPI Authentication Key

Click Save
- Blue button: Save

*Verify Variable*

You should now see:

<img width="426" height="81" alt="image" src="https://github.com/user-attachments/assets/f14735b3-c0e1-4bec-a60a-1ed937c404d7" />

*Test Variable*

From Airflow:

Admin
- → Variables

Verify: NEWS_API_KEY exists.

*What Happens During DAG Execution*

When the DAG starts: newsapi_data_to_gcs

Airflow executes:

fetch_news_data()

Inside that function:

api_key = Variable.get("NEWS_API_KEY")

reads the key from Airflow Variables.

Then:

<img width="299" height="249" alt="image" src="https://github.com/user-attachments/assets/cb4b010c-dae3-4fa3-b028-28b89009cfe0" />

*Expected Result*

After saving the variable:

NEWS_API_KEY = your_actual_newsapi_key

the first Airflow task:

**newsapi_data_to_gcs**

will be able to authenticate with NewsAPI and download articles successfully.

Next step after this is complete: Configure the **Google Cloud credentials** and verify the GCS **bucket snowflake-projects-test-gds exists** before running the DAG.


**Step 2 — Google Cloud Storage**

Open Google Cloud Console. Go to Cloud Storage.

Click Buckets.

Create or verify this bucket:
- **snowflake-projects-test-gds**

Inside the bucket, create this folder:
- news_data_analysis/

This is where **fetch_news.py** uploads Parquet files.*

**Step 3 Snowflake setup**

Open Snowflake Snowsight.

Go to Worksheets. Click + Worksheet.

Open **snowflake_commands.sql.**. Copy all SQL.

Paste it into the worksheet. Run it.

This creates:

<img width="333" height="112" alt="image" src="https://github.com/user-attachments/assets/0a201b8b-4d8a-47e3-a99c-f8b6c818969a" />

After running the storage integration command, Snowflake may show a service account. Give that service account access to your GCS bucket.

**Step 4 — Airflow files**

In your Airflow project, put these two files inside the **dags folder**:
- news_api_airflow_job.py
- fetch_news.py

The DAG imports this function:

<img width="267" height="72" alt="image" src="https://github.com/user-attachments/assets/d00ba1cb-ae9e-40dd-8686-19a63d59370d" />

 So both files must be in the same DAG/import path.

**Step 5 — Airflow GUI: create NewsAPI variable**

Open Airflow UI: http://localhost:8080. Login.

Go to Admin. Click Variables. Click +.

Enter:
- Key: NEWS_API_KEY
- Value: your NewsAPI key

Click Save.

We did this previously just scroll upp and check it out.

**Step 6 — Airflow GUI: create Snowflake connection**

Go to Admin. Click Connections. Click +.

Fill in:
- Connection Id: snowflake_conn
- Connection Type: Snowflake
- Description: Snowflake Connection
- Schema: PUBLIC
- Login: your Snowflake username. Example: Alejandro
- Password: your Snowflake password. Example: *********

In Extra, use:

<img width="281" height="171" alt="image" src="https://github.com/user-attachments/assets/d4d89d12-ce68-4388-8acf-150bc5d9803c" />

Then click Save.

Your screenshot is exactly this step.

*What and where is Extra.*

Scroll down to the bottom of the page. You will see a large text box labeled:
- Extra

The Extra field stores additional Snowflake settings that Airflow needs but that do not fit into the standard fields. Think of it as a place to store Snowflake-specific configuration.

*Paste This Into Extra*

Copy and paste exactly:

<img width="314" height="167" alt="image" src="https://github.com/user-attachments/assets/6cb8b956-febe-4cc1-ac5d-0f1ce6fa72bc" />

*Where Do These Values Come From?*

*account*

From your Snowflake URL. Example:
- https://guxyhix-bq53873.snowflakecomputing.com

The account is:
- guxyhix-bq53873

*warehouse*

Snowflake warehouse name. Usually:
- COMPUTE_WH

You can verify in Snowflake:
- SHOW WAREHOUSES;

*database*

The database created earlier. Example: *news_api*

You can verify:
- SHOW DATABASES;

*role*

The role used by Airflow. Usually:
- ACCOUNTADMIN

You can verify:
- SHOW ROLES;

*insecure_mode*

Leave: false

This means SSL certificate verification is enabled.

*Save*

After filling everything:
- Scroll to the bottom.
- Click Save.

Airflow creates a connection named: **snowflake_conn**

*What Airflow Uses This Connection For*

When your DAG runs:

<img width="251" height="72" alt="image" src="https://github.com/user-attachments/assets/dcebecaf-27e8-4af1-a93c-8b3166c7d433" />

Airflow automatically:
- Reads the username/password.
- Reads the Snowflake account.
- Connects to Snowflake.
- Executes SQL commands.
- Loads NewsAPI data into Snowflake tables.

So the flow becomes:

<img width="236" height="180" alt="image" src="https://github.com/user-attachments/assets/0a69d4c1-2507-4d90-b308-eaaa07790610" />

*If you don't see the "Extra" field*

Scroll all the way to the bottom of the connection form. In some Airflow versions it appears as:
- Extra or Extra JSON

Paste the JSON there exactly as shown above.

Lets continue.

**Step 7 — Run the DAG**

Go to DAGs in Airflow.

Find:
- newsapi_data_processing_dag

Turn it ON.

Click the DAG name.

Click Trigger DAG.

Watch the task boxes.

The task order is:

<img width="255" height="159" alt="image" src="https://github.com/user-attachments/assets/aa4a60de-1f05-46b4-b5ba-31d1be088c62" />

The last two tasks run after the Snowflake copy task.
 
**End-to-end workflow**

- Airflow starts the DAG
- **fetch_news.py** calls NewsAPI
- News articles are cleaned
- Data is saved as a .parquet file
- Parquet file is uploaded to GCS
- Snowflake reads the Parquet file from the GCS external stage
- Data is copied into:
  - news_api.PUBLIC.news_api_data
- Snowflake creates analytics tables:
  - news_api.PUBLIC.summary_news
  - news_api.PUBLIC.author_activity

**Final output tables**

Check these in Snowflake:

<img width="328" height="144" alt="image" src="https://github.com/user-attachments/assets/53164472-bd36-444b-8a3a-25644d3c05a1" />

**summary_news** shows article counts by source.
**author_activity** shows article counts by author.


 






