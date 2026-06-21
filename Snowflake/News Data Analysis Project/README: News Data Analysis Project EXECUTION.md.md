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

<img width="650" height="256" alt="image" src="https://github.com/user-attachments/assets/dee99cd8-33ad-42f2-8d42-1cd52227a95e" />




















