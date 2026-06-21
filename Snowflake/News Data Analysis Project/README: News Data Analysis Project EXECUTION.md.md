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
- C:\airflow-news-project\snowflake_commands.sql
- C:\airflow-news-project\README.md
- C:\airflow-news-project\airflow_snowflake_connection.png
- C:\airflow-news-project\config\gcp-key.json

Do not upload snowflake_commands.sql to Airflow. You run it inside Snowflake Snowsight.

**Exact GUI execution steps**

*Step 1 — NewsAPI*

Go to NewsAPI website. Create an account. Copy your API key.

You will save it later in Airflow as:
- NEWS_API_KEY

Lets explain this in detail.

You are currently at the Snowflake Connection setup screen in Airflow. Before this connection works, you must first create and save your NewsAPI key in Airflow because fetch_news.py retrieves it using:

<img width="291" height="65" alt="image" src="https://github.com/user-attachments/assets/ceb7c1b0-0546-4caa-af31-1185d2ef0c77" />


 










