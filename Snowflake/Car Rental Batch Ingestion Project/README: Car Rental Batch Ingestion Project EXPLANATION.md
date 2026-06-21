I have this project Car Rental Batch Ingestion Project.

<img width="675" height="276" alt="image" src="https://github.com/user-attachments/assets/99082a0a-3854-46f4-a42c-571a2ce74b45" />

<img width="750" height="152" alt="image" src="https://github.com/user-attachments/assets/ace01b44-9ccb-4279-980f-ae42f24bee31" />

<img width="718" height="208" alt="image" src="https://github.com/user-attachments/assets/941b55cb-eb3a-4bba-aa41-44ce5e02010d" />

<img width="733" height="162" alt="image" src="https://github.com/user-attachments/assets/beaf08b1-0768-4be9-b9ae-39390a66f596" />

<img width="747" height="145" alt="image" src="https://github.com/user-attachments/assets/2e8c37e1-e30b-416c-a38c-0288b2e41176" />



This is a Car Rental Batch Ingestion Project. It uses **GCS → Airflow → Dataproc Spark → Snowflake**. The README says the pipeline processes daily car rental JSON data and customer CSV data, uses SCD Type 2 for customers, transforms rentals in Spark, and loads analytics tables into Snowflake.


**What each folder/file is for**

*airflow_job/*
- Contains **car_rental_airflow_dag.py**. Upload this to Airflow / Cloud Composer DAGs folder. It controls the full workflow: gets execution date, updates customer SCD2 records in Snowflake, inserts customers, then submits the Spark job to Dataproc.

*spark_job/*
- Contains **spark_job.py**. Upload this to Google Cloud Storage, because Dataproc will run it from GCS. It reads rental JSON from GCS, validates/transforms it, joins Snowflake dimensions, and writes to rentals_fact.

*data/*

Upload these files to GCS:
- **car_rental_20250903.json**
- **car_rental_20250904.json**
- **customers_20250903.csv**
- **customers_20250904.csv**

The JSON files are rental transactions with rental_id, customer_id, car details, rental dates, locations, amount, and quantity.

*jar_files/*

Upload both JARs to GCS, not Snowflake:
- **snowflake-jdbc-3.16.0.jar**
- **spark-snowflake_2.12-2.15.0-spark_3.4.jar**

These are needed by Dataproc Spark so Spark can connect to Snowflake.

*snowflake_dwh_setup.sql*
- Run this inside Snowflake worksheet. It creates the database, dimensions, fact table, stage, file format, and sample dimension data.

*README.md*
- Documentation and architecture explanation.

2. Correct upload locations

Use this structure in your GCS bucket:

<img width="384" height="325" alt="image" src="https://github.com/user-attachments/assets/ccc5edc3-9d6b-4fe7-8f98-a6906ad5b126" />

Upload **car_rental_airflow_dag.py** here:
- Cloud Composer / Airflow DAGs folder

Run **snowflake_dwh_setup.sql** here:
- Snowflake → Worksheets

**Snowflake GUI execution**

Open Snowflake. Go to Worksheets. Click + Worksheet.

Open **snowflake_dwh_setup.sql.**

Copy all code. Paste it into the worksheet.

Select warehouse:
- COMPUTE_WH
 
Click Run All.

Confirm tables were created:

<img width="297" height="105" alt="image" src="https://github.com/user-attachments/assets/c8171218-99ef-48bf-aa98-9174e41e45ec" />

You should see tables like:
- location_dim
- car_dim
- date_dim
- customer_dim
- rentals_fact

**GCS GUI upload steps**

Open Google Cloud Console. Search Cloud Storage. Click Buckets.

Open your bucket:
- **snowflake-projects-test-gds**

Create folder: car_rental_data

Inside it, create:
- **car_rental_daily_data**
- **customer_daily_data**

Upload JSON files to:
- **car_rental_data/car_rental_daily_data/**

Upload CSV files to:
- **car_rental_data/customer_daily_data/**

Go back to bucket root. Create:
- **car_rental_spark_job**

Upload:
- **spark_job.py**

Create:
- **snowflake_jars**

Upload both .jar files there.

**Dataproc GUI setup**

Open Google Cloud Console. Search Dataproc.
- Click Clusters.
- Click Create cluster.

Choose Cluster on Compute Engine.

Cluster name: **hadoop-dev-new**

Region:
- us-central1
- Use standard/default settings.

Click Create.

Wait until status becomes Running.

The Airflow DAG is hardcoded to use cluster hadoop-dev-new, project dev-sunset-468907-e9, and region us-central1.

**Airflow / Composer GUI setup**

*Upload DAG*

Open Google Cloud Console.

Search Composer.

Open your Composer environment.

Find DAGs folder.

Click the GCS DAGs folder link.

Upload:
- **car_rental_airflow_dag.py**

Lets explain this in detail.

*Open Google Cloud Console*

Open your browser. Go to:
- https://console.cloud.google.com

Log in with your Google account.

*Open Cloud Composer*

In the search bar at the top, type: Composer

Click: Cloud Composer

You will see your Composer environments.

Example:
- Environment
- composer-dev
- airflow-prod
- car-rental-composer

*Open Your Composer Environment*

Click your Composer environment.
- Example: **car-rental-composer**
 
Wait for the environment page to open.

*Open the DAGs Folder*

Inside the Composer environment page: Find the section:
- Environment Configuration

Locate: DAGs Folder

You will see a GCS path similar to: gs://composer-bucket-xxxxx/dags

Click the DAGs Folder link.

*Open Cloud Storage Bucket*

Google automatically opens the Composer bucket.

You should now see something similar to:

composer-bucket-xxxxx
└── dags/

*Upload the DAG File*

Open the dags folder.

Click: Upload Files (top menu). Browse your computer. Select:
- **car_rental_airflow_dag.py**

Click: Open

Wait until upload finishes.

You should see:

<img width="221" height="52" alt="image" src="https://github.com/user-attachments/assets/94039069-600a-4963-97d1-d774a6a76b9d" />

*Verify Upload*

After upload: ; Return to Composer Environment page.

Click: Airflow UI

Airflow opens in a new tab.

*Verify DAG Appears*

In Airflow:; Click: DAGs

Search: **car_rental**

You should see:
- **car_rental_data_pipeline**

This DAG was defined in your file.

*If DAG Does Not Appear*

Wait 2–5 minutes.

Airflow scans the dags/ folder periodically.

Then: Refresh Airflow UI.

Search again: **car_rental_data_pipeline**

*What Happens After Upload?*

Once uploaded:

<img width="401" height="502" alt="image" src="https://github.com/user-attachments/assets/2b617d6c-61b4-41aa-9ec7-ae236bc3a085" />

which matches the workflow defined in **car_rental_airflow_dag.py.**

**Expected Result**

After completing this step, you should be able to open Airflow UI and see:

**car_rental_data_pipeline**

listed under DAGs and ready to be triggered manually.

**Create Snowflake connection**

Open Airflow UI.

Go to Admin. Click Connections. Click +.

Fill:
- Connection Id: snowflake_conn
- Connection Type: Snowflake
- Schema: PUBLIC
- Login: your Snowflake username (this could be Alejandro)
- Password: your Snowflake password (choose one) 

In Extra, put:

<img width="374" height="153" alt="image" src="https://github.com/user-attachments/assets/169fad04-1f6c-4e5b-88db-540e274d4aed" />

Click Save.

**Run the project in Airflow GUI**

Open Airflow UI. lick DAGs.
- Find: **car_rental_data_pipeline**
 
Turn the DAG ON.

Click the DAG name.

Click Trigger DAG.

Add configuration: For September 3:

<img width="302" height="100" alt="image" src="https://github.com/user-attachments/assets/1b89dec1-28b4-451c-a92f-d5cd23870c3d" />

Click Trigger.

Watch tasks run in this order:

<img width="234" height="149" alt="image" src="https://github.com/user-attachments/assets/b8b1ebd5-183d-4279-ad23-15c728235452" />

The DAG uses this exact sequence.

Then repeat for September 4:

<img width="306" height="116" alt="image" src="https://github.com/user-attachments/assets/66665dad-bf8b-48dc-9bea-b14feac6f259" />

**End-to-end architecture**

<img width="426" height="462" alt="image" src="https://github.com/user-attachments/assets/c7cda562-08db-4316-87e2-179b221e028a" />

**Final result**

After both dates run successfully, check Snowflake:

<img width="321" height="140" alt="image" src="https://github.com/user-attachments/assets/3eba314e-86c2-4606-ba5b-d1d4a6181fff" />

Your final warehouse will have customer history in **customer_dim** and rental transactions in **rentals_fact.**


 


 

