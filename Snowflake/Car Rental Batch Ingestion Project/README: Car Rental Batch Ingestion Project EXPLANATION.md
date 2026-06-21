I have this project Car Rental Batch Ingestion Project.

<img width="675" height="276" alt="image" src="https://github.com/user-attachments/assets/99082a0a-3854-46f4-a42c-571a2ce74b45" />

<img width="750" height="152" alt="image" src="https://github.com/user-attachments/assets/ace01b44-9ccb-4279-980f-ae42f24bee31" />

<img width="718" height="208" alt="image" src="https://github.com/user-attachments/assets/941b55cb-eb3a-4bba-aa41-44ce5e02010d" />

<img width="733" height="162" alt="image" src="https://github.com/user-attachments/assets/beaf08b1-0768-4be9-b9ae-39390a66f596" />

<img width="747" height="145" alt="image" src="https://github.com/user-attachments/assets/2e8c37e1-e30b-416c-a38c-0288b2e41176" />



This is a Car Rental Batch Ingestion Project. It uses **GCS → Airflow → Dataproc Spark → Snowflake**. The README says the pipeline processes daily car rental JSON data and customer CSV data, uses SCD Type 2 for customers, transforms rentals in Spark, and loads analytics tables into Snowflake.


**What each folder/file is for**

*airflow_job/*
- Contains car_rental_airflow_dag.py. Upload this to Airflow / Cloud Composer DAGs folder. It controls the full workflow: gets execution date, updates customer SCD2 records in Snowflake, inserts customers, then submits the Spark job to Dataproc.

*spark_job/*
- Contains spark_job.py. Upload this to Google Cloud Storage, because Dataproc will run it from GCS. It reads rental JSON from GCS, validates/transforms it, joins Snowflake dimensions, and writes to rentals_fact.

*data/*

Upload these files to GCS:
- car_rental_20250903.json
- car_rental_20250904.json
- customers_20250903.csv
- customers_20250904.csv

The JSON files are rental transactions with rental_id, customer_id, car details, rental dates, locations, amount, and quantity.

*jar_files/*

Upload both JARs to GCS, not Snowflake:
- snowflake-jdbc-3.16.0.jar
- spark-snowflake_2.12-2.15.0-spark_3.4.jar

These are needed by Dataproc Spark so Spark can connect to Snowflake.

*snowflake_dwh_setup.sql*
- Run this inside Snowflake worksheet. It creates the database, dimensions, fact table, stage, file format, and sample dimension data.

*README.md*
- Documentation and architecture explanation.

2. Correct upload locations

Use this structure in your GCS bucket:

<img width="384" height="325" alt="image" src="https://github.com/user-attachments/assets/ccc5edc3-9d6b-4fe7-8f98-a6906ad5b126" />







