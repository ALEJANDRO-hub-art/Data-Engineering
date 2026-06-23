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

**End-to-End Architecture**

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



















































