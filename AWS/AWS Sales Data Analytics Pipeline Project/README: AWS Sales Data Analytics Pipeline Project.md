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

**7. Test run_athena_query Lambda**

Open Lambda **run_athena_query.**

Click Test.

- Event name: testAthenaRun
 
Event JSON:

<img width="146" height="53" alt="image" src="https://github.com/user-attachments/assets/47938d35-2ea0-4eb7-bac3-819f56dfe469" />

Click Test.

You should get a response containing:

<img width="217" height="91" alt="image" src="https://github.com/user-attachments/assets/5dd77258-7da3-4dff-bde0-78a8b4b066b8" />

Copy that ID.

**8. Create Lambda: check Athena query status**

Go to Lambda. Click Create function.
- Function name: **check_athena_query_status**
- Runtime: Python 3.11

Paste the code from: **check_athena_query_status.py**

Click Deploy.

**9. Test check query status Lambda**

Use this test event:

<img width="341" height="90" alt="image" src="https://github.com/user-attachments/assets/01e1b969-2f55-4246-88e7-4250660f8a5a" />

If successful, it returns the S3 results location:

<img width="349" height="105" alt="image" src="https://github.com/user-attachments/assets/32c37461-51ae-4dbe-8c5a-b90dd41243b4" />

**Exact GUI Steps — Test check_athena_query_status Lambda**

*Step 1 — Open Lambda Console*

Login to AWS Console. In the search bar, type: Lambda

Click Lambda.

*Step 2 — Open the Function*

Under Functions click: **check_athena_query_status**

You should now see:
- Code
- Test
- Monitor
- Configuration
- Aliases
- Versions

*Step 3 — Create a Test Event*

At the top-right of the Lambda page: Click: Test ▼

Then click: Configure test event

*Step 4 — Enter Test Event Information*

Event Name: Type: **CheckAthenaQuery**

Event JSON

Delete everything in the editor and paste:

<img width="340" height="93" alt="image" src="https://github.com/user-attachments/assets/e17eb996-24c3-4398-ac01-4b395f6a2e82" />

Example:

<img width="380" height="106" alt="image" src="https://github.com/user-attachments/assets/bdba78a1-83f8-4a16-9649-1fc0ccfaf9b3" />

*Step 5 — Where do I get the Query Execution ID?*

Go to:

Lambda
- → run_athena_query
- → Test

After running the Lambda you will see output similar to:

<img width="449" height="116" alt="image" src="https://github.com/user-attachments/assets/ea9cbdec-92c4-49cd-9672-301a2f2a7382" />

Copy: 
- **12345678-abcd-1234-abcd-1234567890ab**

Paste it into:

<img width="365" height="108" alt="image" src="https://github.com/user-attachments/assets/e1c458ca-fff6-43d9-88be-1722bcbbb637" />

*Step 6 — Save the Test Event*

Click: Save

AWS creates the test event.

*Step 7 — Run the Test*

Click the orange button: Test (near the top-right.)

Lambda executes.

*Step 8 — View Results*

Scroll down to: Execution Results

If successful you should see:

{
  "statusCode": 200,
  "body": "{\"query_execution_id\":\"12345678-abcd-1234-abcd-1234567890ab\",\"status\":\"SUCCEEDED\",\"s3_output\":\"s3://sales-data-analysis-gds-de/results/...\"}"
}

**Alternative Method (Athena GUI)**

If you forgot the Query Execution ID:

Open AWS Console.

- Search: Athena
- Open: Query Editor
 
Click: Recent Queries or Query History
- Select your query. Copy: Query Execution ID. Example: 12345678-abcd-1234-abcd-1234567890ab

Use it in the Lambda test event.

*Step 9 — Open the Athena Results File*

If the Lambda returns:

<img width="435" height="112" alt="image" src="https://github.com/user-attachments/assets/d003ee80-097e-41a0-82af-9c39c2cd55fd" />

Go to:

AWS Console
→ S3
→ sales-data-analysis-gds-de
→ results

You will see: 12345678-abcd.csv

Click the file and then: Download

This CSV contains the output of the Athena query:

<img width="265" height="165" alt="image" src="https://github.com/user-attachments/assets/d5771842-1035-427d-a08a-86b8384cce09" />

which gives sales totals, order counts, and average sales grouped by year and order status.

**Optional RDS MySQL part**

Use **connect_rds.py** only if your project also requires RDS MySQL.

**GUI steps**

Search RDS. Create a MySQL database. Search Secrets Manager.
- Create a secret named: **rds_mysql_creds**

Secret values must match the code:

<img width="233" height="131" alt="image" src="https://github.com/user-attachments/assets/cc5a9d13-aca0-49ed-a51d-35852cfdb782" />

Run **connect_rds.py** from your computer, EC2, or Lambda.

It creates this database:
- GDSdev

Final execution order
- 1 Upload sales_data.csv to S3 raw/
- 2 Create Glue database sales_db
- 3 Run Glue crawler
- 4 Confirm Athena table sales_data_raw
- 5 Create run_athena_query Lambda
- 6 Run Lambda and copy query_execution_id
- 7 Create check_athena_query_status Lambda
- 8 Check query status
- 9 Open S3 results/ and download Athena result CSV
- 10 Optional: run connect_rds.py to create RDS MySQL database




