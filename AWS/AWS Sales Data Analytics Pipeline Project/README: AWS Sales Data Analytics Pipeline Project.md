I have this project AWS Sales Data Analytics Pipeline Project

<img width="678" height="231" alt="image" src="https://github.com/user-attachments/assets/756a9774-4f37-4ccc-a314-91a306f59e21" />

<img width="640" height="214" alt="image" src="https://github.com/user-attachments/assets/2b1d0ecb-475c-4532-b81d-62845d79ecc7" />

<img width="646" height="168" alt="image" src="https://github.com/user-attachments/assets/02c3d47a-9c75-473c-842a-db8addb00671" />

Project name: **AWS Sales Data Analytics Pipeline**

I’ll treat this as one AWS sales analytics project using **S3, Glue/Athena, Lambda, RDS MySQL, and Secrets Manager**. I’ll inspect the uploaded files first so the steps match your exact code.

This project uploads sales CSV data to Amazon S3, catalogs it with AWS Glue / Athena, runs an Athena SQL aggregation from Lambda, checks query status with another Lambda, and optionally connects to RDS MySQL using credentials stored in Secrets Manager.

**What each file does**

<img width="655" height="314" alt="image" src="https://github.com/user-attachments/assets/0365e126-2e68-41d8-98bf-44feaec7d0ef" />

Recommended S3 structure

Create one S3 bucket: **sales-data-analysis-gds-de**

Inside the bucket, create folders:
- raw/
- results/
- scripts/

Upload files like this:
 
```text
sales-data-analysis-gds-de/
├── raw/
│   └── sales_data.csv
├── results/
└── scripts/
    ├── run_athena_query.py
    ├── check_athena_query_status.py
    └── connect_rds.py
```

**End-to-end architecture**

sales_data.csv
<br>⬇️
<br>Amazon S3 raw/
<br>⬇️
<br>AWS Glue Crawler
<br>⬇️
<br>Glue Data Catalog Database: **sales_db**
<br>⬇️
<br>Athena Table: **sales_data_raw**
<br>⬇️
<br>Lambda: run_athena_query
<br>⬇️
<br>Athena SQL Aggregation
<br>⬇️
<br>S3 results/
<br>⬇️
<br>Lambda: check_athena_query_status
<br>⬇️
<br>Query result file available in S3



Optional:
Secrets Manager
<br>⬇️
<br>**connect_rds.py**
<br>⬇️
<br>Amazon RDS MySQL
<br>⬇️
<br>Creates database GDSdev

**Step-by-step GUI execution**

**1. Create the S3 bucket**

Go to AWS Console. Search S3. Click Create bucket.
- Bucket name: **sales-data-analysis-gds-de**
- Region: us-east-1

Click Create bucket.

Open the bucket.

Click Create folder. Create:
- raw
- results
- scripts
 
Open raw/. Click Upload.
- Upload: **sales_data.csv**

**2. Create Glue database**

Search AWS Glue. Go to Data Catalog.

Click Databases. Click Add database.
- Database name: **sales_db**

Click Create database.

**3. Create Glue crawler**

In AWS Glue, go to Crawlers. Click Create crawler.
- Name: **sales-data-crawler**

Data source: **S3.**

S3 path: **s3://sales-data-analysis-gds-de/raw/**

Choose or create an IAM role for Glue.

Target database: **sales_db**

Table name should become something like: **sales_data_raw**

Click Create crawler.

Click Run crawler.

**4. Verify Athena table**

Search Athena. Go to Query editor.

Select database: **sales_db**

Confirm table exists: **sales_data_raw**

Run:

<img width="241" height="87" alt="image" src="https://github.com/user-attachments/assets/be601a4f-6acf-4323-a540-2ff62e99f704" />

**5. Create Lambda: run Athena query**

Search Lambda. Click Create function.

Choose Author from scratch.
- Function name: **run_athena_query**
- Runtime: **Python 3.11**

Click Create function.

Open the code editor.

Paste the code from: **run_athena_query.py**

Click Deploy.

**6. Add Lambda permissions**

Your Lambda role needs access to:
- Athena
- S3
- Glue Data Catalog
- CloudWatch Logs

Attach these policies for practice/lab use:
- AmazonAthenaFullAccess
- AmazonS3FullAccess
- AWSGlueConsoleFullAccess
- CloudWatchLogsFullAccess











