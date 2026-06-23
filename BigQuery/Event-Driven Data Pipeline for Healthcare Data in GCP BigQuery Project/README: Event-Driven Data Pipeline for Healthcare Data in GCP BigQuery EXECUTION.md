I have this project **Event-Driven Data Pipeline for Healthcare Data in GCP BigQuery Project**.

<img width="628" height="278" alt="image" src="https://github.com/user-attachments/assets/dc49f69b-0237-4f9c-abd9-752a0c0190cc" />

**Objective**
Design and implement an event-driven data pipeline in Google Cloud Platform (GCP) for processing healthcare data with a focus on cancer patients.

**● Requirements**

**● Data Source and Format:**
- ○ Daily receipt of clinical data as JSON files in a GCP bucket.
- ○ File Naming Convention: clinical_data_yyyy_mm_dd.json.

**● Event-Driven Ingestion:**
- ○ Automate data ingestion upon file arrival in the GCP bucket.

**● Target Storage:**
- ○ Data is to be loaded into a BigQuery table (You can create schema design as per your need and assumptions)

**● Data Filtering:**
- ○ Ingest only data related to cancer patients.

**● Data Validation:**
- ○ Ensure patient identifiers (like patient ID) are present and unique.
- ○ Validate date fields (e.g., date of diagnosis) for format correctness.
- ○ Check mandatory fields such as patient ID, diagnosis code, and hospital ID.
- ○ Confirm diagnosis codes are specific to cancer.
- ○ Verify data types and formats for all fields (e.g., numeric values, text strings).
- ○ Exclude records with incomplete or inconsistent data.

**● Sample Data File:**
- ○ A sample JSON file representing clinical data has been provided, refer that
- ○ Write script to generate 3-4 mock data files with random values to implement and test your logic

**● Hint - Suggested GCP Services:**
- ○ GCP Bucket
- ○ GCP Functions
- ○ Dataflow
- ○ BigQuery

**● Deliverables**
- ○ Code, Data files, Configurations, Metadata files
- ○ Documentation explaining the setup and complete execution of the application.

----------------------------------------------------------------------------------------------------------------------------------------

I’ll treat this as a GCP healthcare event-driven pipeline: **GCS receives JSON files, Cloud Function triggers Dataflow, Dataflow filters/transforms, and BigQuery stores cancer-patient records.**

I checked the key files. The main important detail is that the Cloud Function has a hardcoded project ID, so you must replace it with your own GCP Project ID before deployment.

**Project summary**

This is an event-driven healthcare data pipeline in GCP. A JSON clinical file lands in Cloud Storage, a Cloud Function automatically starts a Dataflow template, Dataflow applies a JavaScript filter, and only cancer patient records are loaded into BigQuery. The assignment specifically requires JSON files in GCS, automatic ingestion, cancer-only filtering, validation, and BigQuery storage.

**What each file does**

<img width="654" height="449" alt="image" src="https://github.com/user-attachments/assets/4b9f18b9-9e30-4ad1-a452-843849ee53ef" />

**GCS bucket folder structure**

Create one GCS bucket, for example:

<img width="293" height="158" alt="image" src="https://github.com/user-attachments/assets/88152088-31de-4e3a-bd0c-8ed09063af34" />

Upload files like this:
- **bq_health_schema.json**       ➜ schema/bq_health_schema.json
- **transform.js**                ➜ transform_script/transform.js
- **mock_data_20230101.json**     ➜ bucket root OR input/
- **sample_clinical_data...json** ➜ bucket root OR input/

**Step-by-step execution**

**Step 1 — Create BigQuery dataset**

Go to Google Cloud Console. Search BigQuery.

Click your project. Click ⋮ View actions beside your project.

Click Create dataset.
- Dataset ID: **healthcare_app**
- Location: us-central1

Click Create dataset.

**Step 2 — Create BigQuery table**

In BigQuery, click **SQL workspace**. Paste the content of **create_table.sql**:

<img width="292" height="182" alt="image" src="https://github.com/user-attachments/assets/d02fa4cd-fe3e-478e-a7f9-3fac73c40f79" />

Click Run.

**Step 3 — Create Cloud Storage bucket**

Go to Cloud Storage. Click Create bucket.
- Name it, for example: **healthcare-pipeline-bucket**
- Region: us-central1

Click Create.

**Step 4 — Create folders in bucket**

Inside the bucket, click Create folder and create:
- schema
- transform_script
- templates
- temp

**Step 5 — Upload schema file**

Upload: **bq_health_schema.json** ➜ to: **schema/bq_health_schema.json**

**Step 6 — Upload transform file**

Upload: **transform.js** ➜ to: **transform_script/transform.js**

This file keeps cancer records only. Non-cancer records like HIV, Asthma, or Pneumonia are ignored.

**Step 7 — Create Dataflow template**

Use Google’s built-in template:
- **Text Files on Cloud Storage to BigQuery**

In the bucket, the Cloud Function expects the template here:
- gs://YOUR_BUCKET/**templates/GCS_Text_to_BigQuery**

**Option A (Recommended)** — Use Google's Existing Template

*1. Open Dataflow*

In Google Cloud Console:

☰ Navigation Menu → Dataflow

*2. Click*

CREATE JOB FROM TEMPLATE (top of the page)

*3. Select Template Category*

Choose: Google Provided Templates

*4. Search Template*

In the search box type: Text Files on Cloud Storage to BigQuery
- Select: **Text Files on Cloud Storage to BigQuery**

*5. Fill Temporary Values*

You are only testing the template exists.

Example:
- Job Name: **healthcare-test**
- Input File Pattern: **gs://your-bucket/sample_clinical_data_2023_12_05.json**
- Output Table: your-project:healthcare_app.patients
- BigQuery Loading Temporary Directory:**gs://your-bucket/temp**
- JSONPath: **gs://your-bucket/schema/bq_health_schema.json**
- Javascript UDF Path: **gs://your-bucket/transform_script/transform.js**
- Javascript Function Name: **transform**

*6. Click*
RUN JOB

Wait until the job completes.

*7. Verify*

Go to: Dataflow

You should see: **healthcare-test**. Status: Succeeded

**Important**

Your Cloud Function automatically launches the same template later.

When a JSON file arrives:

Cloud Storage
      ↓
Cloud Function
      ↓
Google Dataflow Template
      ↓
BigQuery

The Cloud Function launches the template using:

<img width="326" height="67" alt="image" src="https://github.com/user-attachments/assets/a8846856-156a-46a1-bbf7-8a85e4138f67" />

which means after deployment you do not manually run Dataflow anymore. The **file upload triggers everything automatically (the above step in the architecture Cloud Storage).**





























