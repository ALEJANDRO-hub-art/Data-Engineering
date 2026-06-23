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


























