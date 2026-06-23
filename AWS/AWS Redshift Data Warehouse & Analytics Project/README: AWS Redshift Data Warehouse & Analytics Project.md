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

sadasdsad












































