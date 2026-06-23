I have this project AWS Redshift Data Warehouse & Analytics Project.

<img width="631" height="213" alt="image" src="https://github.com/user-attachments/assets/b5ab3d30-7c53-49c0-abf7-0f0eea522ab7" />

<img width="627" height="209" alt="image" src="https://github.com/user-attachments/assets/c507202e-0965-48d1-b6a4-c39b7578081b" />

<img width="622" height="209" alt="image" src="https://github.com/user-attachments/assets/02f0f31c-5b8c-4a4a-b1e7-56d67b0bc744" />

This is one AWS Redshift project, not multiple unrelated mini-projects.

Project Name: **AWS Redshift Data Warehouse & Analytics Project**

What the Project Does

The project demonstrates several core Amazon Redshift capabilities:
- Upload sales data into Amazon S3.
- Load data from S3 into Redshift tables using COPY.
- Create Redshift schemas and tables.
- Run analytical SQL queries.
- Export query results back to S3 using UNLOAD.
- Create Redshift Spectrum external tables.
- Create and refresh Materialized Views for faster reporting.

Files and Their Purpose

<img width="630" height="227" alt="image" src="https://github.com/user-attachments/assets/40892336-eac0-43e2-92d7-80f308a7152f" />

Lets see the EXECUTION of the project.

I’ll map the uploaded Redshift/S3 files into one clear project execution guide: file placement, purpose, AWS GUI steps, and final architecture.

Project Name: **Amazon Redshift Sales Data Analytics Pipeline**

**What this project does**
- This project loads sales CSV data from Amazon S3 into Amazon Redshift, runs SQL analytics, creates a materialized view, uses Redshift Spectrum for external tables, and exports query results back to S3.

**Where to upload the files**

Upload only the CSV data files to Amazon S3:
- s3://redshift-data-gds-new/input/**sales.csv**
- s3://redshift-data-gds-new/input/**sales_2025_01_11.csv**
- s3://redshift-data-gds-new/input/**sales_2025_01_12.csv**

Keep these files locally or in GitHub:
- **redshift_commands.txt**
- **redshift_query_commands.txt**

You paste/run the SQL commands inside Amazon Redshift Query Editor v2.

<img width="642" height="276" alt="image" src="https://github.com/user-attachments/assets/50044720-0c2b-4376-ba02-63e9d7400734" />

**End-to-End Architecture**

📊 Amazon Redshift Sales Analytics Pipeline

```text
Sales CSV Files
    │
    ▼
Amazon S3 Bucket
    │
    ▼
Amazon Redshift
    │
    ├── COPY Command
    │
    ▼
sales_raw Table
    │
    ├── SQL Analytics
    ├── Materialized Views
    ├── Spectrum External Tables
    │
    ▼
Query Results
    │
    ▼
UNLOAD Command
    │
    ▼
Amazon S3 Output Folder
```

**Step-by-step execution in AWS GUI**

**1. Create S3 bucket** 

Go to: **AWS Console ➜ S3 ➜ Create bucket**

Bucket name: **redshift-data-gds-new**

Create folders:
- input/
- output/

Upload the CSV files (**sales_2025_01_11.csv, sales_2025_01_12.csv, sales.csv**) into:
- input/

**2. Create IAM Role for Redshift**

Go to: **AWS Console ➜ IAM ➜ Roles ➜ Create role**

Choose: AWS Service ➜ Redshift

Attach permissions:
- AmazonS3ReadOnlyAccess
- AmazonS3FullAccess
- AWSGlueConsoleFullAccess

Role name example: **redshift_role**

**3. Create Redshift cluster or Redshift Serverless**

Go to: **AWS Console ➜ Amazon Redshift**

Use either: Provisioned cluster or Redshift Serverless

Make sure the Redshift role is attached.

**4. Open Redshift Query Editor v2**

Go to: **Amazon Redshift ➜ Query Editor v2**

Connect to your database.

Lets explain this in detail.

*Exact GUI Steps — Open Redshift Query Editor v2*

*Step 1 — Open AWS Console*

Go to: https://console.aws.amazon.com

Sign in to your AWS account.

*Step 2 — Open Amazon Redshift*

In the AWS search bar at the top: Type: Redshift

Click: Amazon Redshift

*Step 3 — Verify your Cluster Exists*

In the left menu click: Clusters

You should see something similar to: **sales-redshift-cluster** or **redshift-cluster-1**

Status must be: Available

*Step 4 — Open Query Editor v2*

In the left navigation menu click: Query Editor v2

Location:

```text
Amazon Redshift
├── Dashboard
├── Clusters
├── Serverless
├── Query Monitoring
└── Query Editor v2
```

Click: Query Editor v2

*Step 5 — Connect Account (First Time Only)*

If this is your first time opening Query Editor v2 you'll see: Configure account
- Click: Configure account

Wait for AWS to finish configuration.

*Step 6 — Create Connection*

Click: Create connection or Connect

*Step 7 — Select Connection Type*

You'll see: Connect to database

Choose: Temporary credentials or Database user name and password

For learning projects: Temporary credentials

is easiest.

*Step 8 — Select Cluster*

Under: Cluster or workgroup
- Select: Your Redshift cluster. Example: **sales-redshift-cluster**

*Step 9 — Select Database*

Under: Database
- Enter: **dev**

Most Redshift clusters use:
- dev

by default.

*Step 10 — Select Database User*

Enter: **awsuser**

or the admin username you created when creating the cluster.

Example: **awsuser**

*Step 11 — Connect*

Click: Connect

You should now see:

```text
Editor
┌─────────────────────────────┐
│                             │
│     SQL Editor Window       │
│                             │
└─────────────────────────────┘
```

**5. Create schema**

<img width="235" height="54" alt="image" src="https://github.com/user-attachments/assets/21a2c500-c4b4-4ac6-8238-182ff66e1520" />

**6. Create Redshift table**

<img width="306" height="144" alt="image" src="https://github.com/user-attachments/assets/c40870d1-6fb3-4644-9fd1-43efd92e4f87" />

**7. Load data from S3 into Redshift**

<img width="383" height="133" alt="image" src="https://github.com/user-attachments/assets/9e4a93ea-0cae-4b30-bff8-f0c75ba5f27b" />

Replace the IAM role ARN with your real Redshift role ARN.

**8. Test the loaded data**

<img width="256" height="64" alt="image" src="https://github.com/user-attachments/assets/f9325ed5-06c4-40b4-a992-bbdc78810ef5" />

**9. Create analytics summary**

<img width="369" height="149" alt="image" src="https://github.com/user-attachments/assets/314c3ae3-4fc8-4c92-bc37-8a3c8f706f2b" />

**10. Query the summary**

<img width="221" height="60" alt="image" src="https://github.com/user-attachments/assets/2cede89d-a211-4398-ae4f-d87a22d31b97" />

**11. Export query results back to S3**

<img width="418" height="164" alt="image" src="https://github.com/user-attachments/assets/425bb6a4-51ac-49f8-8596-8720c96db0bc" />

**End-to-end architecture**

Sales CSV Files
<br>⬇️
<br>Amazon S3 Bucket
<br>⬇️
<br>Redshift COPY Command
<br>⬇️
<br>sales.sales_raw Table
<br>⬇️
<br>SQL Analytics
<br>⬇️
<br>Materialized View
<br>⬇️
<br>Query Results
<br>⬇️
<br>UNLOAD Command
<br>⬇️
<br>Amazon S3 Output Folder



**Final workflow**

Upload sales.csv to S3
<br>⬇️
<br>Create Redshift schema and table
<br>⬇️
<br>Run COPY command
<br>⬇️
<br>Load CSV data into Redshift
<br>⬇️
<br>Run SQL analytics
<br>⬇️
<br>Create materialized view
<br>⬇️
<br>Export results using UNLOAD
<br>⬇️
<br>View output files in S3








































