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

Cloud Storage ➜ Cloud Function ➜ Google Dataflow Template ➜ BigQuery

The Cloud Function launches the template using:

<img width="326" height="67" alt="image" src="https://github.com/user-attachments/assets/a8846856-156a-46a1-bbf7-8a85e4138f67" />

which means after deployment you do not manually run Dataflow anymore. The **file upload triggers everything automatically (the above step in the architecture Cloud Storage).**

**Exact GUI Location Summary**

**Google Cloud Console**  
⬇️  
**Navigation Menu**  
⬇️  
**Dataflow**  
⬇️  
**Create Job From Template**  
⬇️  
**Google Provided Templates**  
⬇️  
**Text Files on Cloud Storage to BigQuery**  
⬇️  
**Run Job**

After this step, the next GUI task is usually deploying the Cloud Function, which connects the bucket upload event to Dataflow.

**Step 8 — Edit Cloud Function file before deploying**

Open **google_cloud_function.py**.

Change this line:

<img width="233" height="65" alt="image" src="https://github.com/user-attachments/assets/ccdaeafb-d9ac-463d-bc6e-26480ff1203a" />

to your real GCP Project ID:

<img width="203" height="63" alt="image" src="https://github.com/user-attachments/assets/b6c88ae5-c70a-4d8d-8659-56ce18d78f27" />

Also confirm this output table is correct:

<img width="304" height="56" alt="image" src="https://github.com/user-attachments/assets/3d8d2741-8d1e-4202-aa7c-b22bc922d3bd" />

The function launches Dataflow in:
- us-central1

and uses the uploaded schema, transform script, and temp folder.

**Cloud Function GUI steps**

Go to Cloud Functions. Click Create function.
- Environment: 2nd gen
- Function name: **start_cf_to_dataflow_to_bq_flow**
- Region: us-central1
- Trigger: Cloud Storage
- Event type: Finalize/Create
- Bucket: **healthcare-pipeline-bucket**
- Runtime: Python 3.11
- Entry point: start_cf_to_dataflow_to_bq_flow
- Upload/paste the code from: **google_cloud_function.py**
- Add dependency in requirements.txt: functions-framework, google-api-python-client (create this .txt file and put it in the project folder)

Click Deploy.

**Upload test data**

After the Cloud Function is deployed, upload:
- **mock_data_20230101.json** or: **sample_clinical_data_2023_12_05.json**

to the bucket root.

Example: **gs://healthcare-pipeline-bucket/mock_data_20230101.json**

That upload triggers the Cloud Function automatically.

**Check Dataflow job**

Go to Dataflow. Click Jobs.

Look for a job like: **health-batch-dataflow-2023-...**

Click the job.

Check that the status becomes: Succeeded

If it fails, check:
- schema path
- transform path
- BigQuery table name
- Cloud Function project ID
- Dataflow permissions

**Check BigQuery output**

Go to BigQuery and run:

<img width="295" height="72" alt="image" src="https://github.com/user-attachments/assets/cb1d7ee3-ebc5-4c5d-aa03-311d4dd30c6f" />

Check cancer-only records:

<img width="279" height="110" alt="image" src="https://github.com/user-attachments/assets/b2546a7c-2009-4ee8-bea3-f71519000ca4" />

Expected diseases include:
- Breast Cancer
- Colon Cancer
- Liver Cancer
- Prostate Cancer
- Stomach Cancer
- Esophageal Cancer
- Colorectal Cancer

Non-cancer diseases should be excluded because the transform function returns null for them.










