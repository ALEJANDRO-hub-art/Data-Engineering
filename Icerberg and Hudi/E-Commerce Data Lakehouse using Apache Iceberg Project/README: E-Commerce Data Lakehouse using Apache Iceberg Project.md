I have this project E-Commerce Data Lakehouse using Apache Iceberg Project. 

<img width="835" height="169" alt="image" src="https://github.com/user-attachments/assets/bf6e953d-af33-4762-9024-881daa95b6ae" />

**What the project does**

This project uses AWS Glue PySpark with Apache Iceberg to create an e-commerce orders table in Amazon S3, register it in AWS Glue Data Catalog, write/append/overwrite/merge data, then read the table and query Iceberg snapshots/time travel.

<img width="624" height="219" alt="image" src="https://github.com/user-attachments/assets/25a4fe92-5fe6-49f1-b8a0-76de3380cc26" />

**End-to-end architecture**

```text
Developer
   ⬇️
AWS Glue Studio
   ⬇️
Glue PySpark Job: glue_iceberg_write.py
   ⬇️
Apache Iceberg Table
   ⬇️
AWS Glue Data Catalog: ecommerce.orders
   ⬇️
Amazon S3 Warehouse: s3://iceberg-warehouse-gds/warehouse/
   ⬇️
Glue PySpark Job: glue_iceberg_read.py
   ⬇️
Read Latest Data + Snapshots + Time Travel
```
**Step-by-step execution**

**Step 1 — Create the S3 bucket**

Go to AWS Console. Search S3. Click Create bucket.
- Bucket name: **iceberg-warehouse-gds**

Keep default settings. Click Create bucket.

Inside the bucket, create this folder:
- **warehouse/**

**Step 2 — Create IAM Role for Glue**

Go to IAM. Click Roles. Click Create role.
- Trusted entity: AWS service.
- Use case: Glue.

Click Next.

Attach policies:
- **AWSGlueServiceRole**
- **AmazonS3FullAccess**
- **AWSGlueConsoleFullAccess**

Role name: **AWSGlueIcebergRole**

Click Create role.

Lets explain this in detail.

**Create IAM Role for AWS Glue (Exact GUI Steps)**

*1. Open IAM*

Log in to AWS Console. In the top search bar, type: IAM
- Click IAM.

*2. Open Roles*

In the left navigation menu:

<img width="201" height="140" alt="image" src="https://github.com/user-attachments/assets/54749c7f-ecea-4a94-b395-d1a3fe4fd20f" />

Click Roles.

*3. Create New Role*

Click the orange Create role button (upper-right corner).

*4. Select Trusted Entity*

You should see:

Trusted entity type
- ○ AWS account
- ● AWS service
- ○ Web identity
- ○ SAML 2.0 federation
- ○ Custom trust policy

Select: AWS service. Click Next.

*5. Select Use Case*

You should see: Use case

In the search box type: Glue
- Select: Glue

The page should look similar to:

<img width="163" height="51" alt="image" src="https://github.com/user-attachments/assets/ddaef6e6-2d31-4171-936e-ec987ce23cb6" />

Click Next.

*6. Attach Permissions*

In the permissions search box, search and add these three policies:

Policy 1
- Search: **AWSGlueServiceRole**. Check the box.

Policy 2
- Search: **AmazonS3FullAccess**. Check the box.

Policy 3
- Search: **AWSGlueConsoleFullAccess**. Check the box.

You should have:
- ☑ **AWSGlueServiceRole**
- ☑ **AmazonS3FullAccess**
- ☑ **AWSGlueConsoleFullAccess**

Click Next.

*7. Name the Role*

- Role name: **AWSGlueIcebergRole**

Description (optional): Role used by AWS Glue Iceberg ETL jobs

Click Next.

*8. Review*

Verify:
- Trusted Entity: AWS Service → Glue

Policies:
- **AWSGlueServiceRole**
- **AmazonS3FullAccess**
- **AWSGlueConsoleFullAccess**

Role Name: **AWSGlueIcebergRole**

*9. Create Role*

Click: Create role

*10. Verify Role Exists*

After creation:

<img width="215" height="62" alt="image" src="https://github.com/user-attachments/assets/c1088984-6d1f-4a9c-9264-6406c67b462e" />

Click the role and confirm the permissions are attached.

You will select this role later when creating:
- **glue_iceberg_write**
- **glue_iceberg_read**

Glue jobs.

**Step 3 — Create Glue write job**

Go to AWS Glue.
- Click ETL jobs.
- Click Script editor.

Select Spark. Click Create.
- Job name: **glue_iceberg_write**
- IAM role: **AWSGlueIcebergRole**
- Glue version: choose Glue 4.0 or Glue 5.0.
- Language: Python 3.

Paste the content of: **glue_iceberg_write.py**

Click Save.

Click Run.

**Step 4 — Confirm table was created**

Go to AWS Glue. Click Data Catalog. Click Databases
.
Look for: **ecommerce**. Open it.

You should see the table: **orders**

**Step 5 — Confirm data in S3**

Go to S3.
- Open bucket: **iceberg-warehouse-gds**
- Open: **warehouse/**

*You should see Iceberg table folders/files created by the Glue job.*


**Step 6 — Create Glue read job**

Go to AWS Glue. 
- Click ETL jobs. 
- Click Script editor.
- Select Spark.

Click Create.

- Job name: **glue_iceberg_read**
- IAM role: **AWSGlueIcebergRole**
- Glue version: use the same version as the write job.

Paste the content of: **glue_iceberg_read.py**

Click Save.

Click Run.

**Step 7 — Check output logs**

Open the Glue job. Go to Runs.
- Click the latest run.
- Click CloudWatch logs.
 
Check the output from: 

<img width="251" height="83" alt="image" src="https://github.com/user-attachments/assets/02e711d0-a89e-4a28-9482-de77f3d62793" />












