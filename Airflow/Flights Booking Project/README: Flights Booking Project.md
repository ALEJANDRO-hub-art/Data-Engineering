I have the following project Flights Booking Project.

<img width="706" height="301" alt="image" src="https://github.com/user-attachments/assets/97cbb044-19cd-4a4b-a989-ea5c604890e2" />

<img width="709" height="149" alt="image" src="https://github.com/user-attachments/assets/4ccd23f0-69e5-4fed-93d6-93de47dbbcac" />

<img width="675" height="158" alt="image" src="https://github.com/user-attachments/assets/44d2ae6a-937b-4a17-9bd9-d7a1e7d19523" />

<img width="642" height="165" alt="image" src="https://github.com/user-attachments/assets/c49aab9b-bbd5-44f5-aae8-82aa150cd750" />

<img width="685" height="191" alt="image" src="https://github.com/user-attachments/assets/ea8bb25a-e67b-4ac8-9e69-be701146374e" />

<img width="675" height="152" alt="image" src="https://github.com/user-attachments/assets/686635dd-82bb-4f5b-af84-e4071c51ac29" />

<img width="647" height="144" alt="image" src="https://github.com/user-attachments/assets/a8cc31f8-d4bd-4fe0-83ba-0819db69e8c2" />


This is one GCP data engineering project:
**GCS → Airflow/Cloud Composer → Dataproc Serverless PySpark → BigQuery**

<img width="690" height="532" alt="image" src="https://github.com/user-attachments/assets/0c880685-1637-432e-94db-ebbb3895cd90" />

<img width="649" height="369" alt="image" src="https://github.com/user-attachments/assets/6a8661f8-f831-489c-9fb5-a8b6c162db7f" />

**GCP GUI setup steps**

Create or open the GCS bucket

Open Google Cloud Console. Go to Cloud Storage. Open bucket:
- airflow-projetcs-gds-dev

Create folder:
- flight-booking-analysis/

Inside it, create:
- source-dev/
- source-prod/
- spark-job/

Upload flight_booking.csv into:
- flight-booking-analysis/source-dev/

The final path must be:
- gs://airflow-projetcs-gds-dev/flight-booking-analysis/source-dev/flight_booking.csv

Lets explain this in detail.

Verify the Upload

Inside the source-dev folder, you should now see:

Name
- flight_booking.csv

Click the file once to verify it exists.

<img width="516" height="189" alt="image" src="https://github.com/user-attachments/assets/8d132cb8-d063-4143-ab5d-1aee56790151" />

**Upload project files to GitHub**

In GitHub:

Open your repository.
- Click Add file → Create new file.

Create these files exactly:
- airflow_job/airflow_job.py
- spark_job/spark_transformation_job.py
- variables/dev/variables.json
- variables/prod/variables.json
- .github/workflows/ci-cd.yaml
- README.md

Paste each uploaded file into the correct path. Commit to the dev branch first.

**Add GitHub secrets**

In GitHub:

Open your repo. Go to Settings. Go to Secrets and variables → Actions. Click New repository secret.

Add:
- GCP_PROJECT_ID = dev-sunset-468907-e9
- GCP_SA_KEY = your service account JSON key

Lets explain this in detail.

Open Repository Settings. Near the top of the repository, click:
- Settings

It is located on the same row as:

Code | Issues | Pull requests | Actions | Projects | Wiki | Security | Insights | Settings

If you do not see Settings, make sure you are the owner of the repository.

Open GitHub Actions Secrets
In the left sidebar, scroll down to the Security section.
- Click: Secrets and variables.

A submenu will expand.
- Click: Actions

You should now be on the page titled:
- Actions secrets and variables

Create the First Secret (GCP_PROJECT_ID)

Click the button:  New repository secret. Under Name, enter:
- GCP_PROJECT_ID

Under Secret, enter:
- dev-sunset-468907-e9

Click: Add secret

Create the Second Secret (GCP_SA_KEY)
- Click: New repository secret

Under Name, enter:
- GCP_SA_KEY

*Leave this page open while you obtain your GCP service account JSON key. You will get this JSON key in the next step*

**Generate the Service Account JSON Key in GCP**

Open IAM & Admin. Open Google Cloud Console:
- https://console.cloud.google.com

Select project:
- dev-sunset-468907-e9
 
Click the ☰ Navigation menu. Go to:

IAM & Admin
- Service Accounts

Create a Service Account (if one doesn't exist)

Otherwise: Click:
- + CREATE SERVICE ACCOUNT
  + 
Service account details

Enter: Service account name: github-actions-deployer

GCP automatically generates the ID.

Example:
- github-actions-deployer@dev-sunset-468907-e9.iam.gserviceaccount.com

Click: CREATE AND CONTINUE

Grant permissions

Under: Grant this service account access to project

Add these roles:

1. Composer Administrator. Search: Composer Administrator
- Select: Cloud Composer Admin

2. Storage Administrator.
- Search: Storage Administrator. Select it.

3. Dataproc Administrator
- Search: Dataproc Administrator. Select it.

4. BigQuery Admin
- Search: BigQuery Admin. Select it.

Click: CONTINUE

Then: DONE

Generate the JSON key

Back on the Service Accounts page: Find:
- github-actions-deployer

Click its email address. Example:
- github-actions-deployer@dev-sunset-468907-e9.iam.gserviceaccount.com

At the top, click:
- KEYS

Then click:
- ADD KEY
    ↓
Create new key

A window appears.

Select: JSON

Then click: CREATE

Download the JSON file

Your browser automatically downloads a file similar to:
- dev-sunset-468907-e9-xxxxxxxxxxxx.json

Example location on Windows: C:\Users\Usuario\Downloads\

Do not rename or edit this file.

Copy the JSON contents

Open the downloaded .json file using: Notepad or VS Code

You'll see something like this:

<img width="630" height="318" alt="image" src="https://github.com/user-attachments/assets/950d705a-429f-4338-bd84-9fe770ee81c8" />

Add it to GitHub

Open your GitHub repository. Go to:

<img width="635" height="371" alt="image" src="https://github.com/user-attachments/assets/3e455345-9112-4142-850d-be2523af0dad" />

Then click: Add secret

Final result

Under Settings → Secrets and variables → Actions, you should now see:
- GCP_PROJECT_ID
- GCP_SA_KEY

Your GitHub Actions workflow can now authenticate to GCP using this service account JSON key.

**Run GitHub Actions deployment**

Go to your GitHub repo. Click Actions.
- Open workflow: Flight Booking CICD

Push/commit to branch:dev

The workflow uploads:
- Airflow variables to Composer
- Spark job to GCS
- DAG to Cloud Composer

Lets explain this in detail.

Run GitHub Actions Deployment (Exact GUI Steps)

This assumes:

GitHub repository already exists. ci-cd.yaml is inside: .github/workflows/ci-cd.yaml

Secrets already exist:
- GCP_PROJECT_ID
- GCP_SA_KEY

Verify the workflow file exists
Open GitHub. Go to:
- https://github.com

Open your repository
- Select: Flights-Booking-Project-Demo

(or whatever name you used)

Above they talk about a workflow named Flight Booking CICD. That is the following:

<img width="576" height="433" alt="image" src="https://github.com/user-attachments/assets/4e0ff45d-4b6e-4b6d-accb-bee1ca7c4364" />

Verify the workflow location

In the repository file tree verify:

<img width="157" height="91" alt="image" src="https://github.com/user-attachments/assets/82744766-4098-40eb-9cea-a6d5853ae890" />

Open GitHub Actions. Click Actions

At the top of the repository click:
- Code
- Issues
- Pull Requests
- Actions
- Projects
- Wiki

Select: Actions

Enable Actions (first time only). If GitHub displays: Get started with GitHub Actions
- Click: Enable Actions

Locate your workflow. Left side panel: You should see:
- Flight Booking CICD

Click it.

Trigger deployment through a commit. Your workflow is configured to run when code is pushed.

Open the dev branch. Near the upper-left area of GitHub: Click branch selector.

You will see:
- main
- dev

Select: dev

Make a small change. Open: README.md
- Click: ✏ Edit

Add a line: Project deployment test

Commit the change.
- Click: Commit changes...

Commit directly to dev.

Select: Commit directly to the dev branch
Click: Commit changes

Watch the deployment run. Return to **Actions**
- Click: Actions

Open the latest run. You should immediately see a new run:
- Flight Booking CICD

with status: Queued or In Progress

Click it.

Open the job. Inside the workflow run click the job name. The job name is the following:

jobs:
  upload-to-dev:

Watch each step execute

You should see green checkmarks appear for:
- Checkout Repository
- Authenticate to GCP
- Upload Spark Job
- Upload Airflow DAG
- Set Airflow Variables
- Deploy Complete

Verify deployment in GCP. Verify DAG upload

Open: Google Cloud Console

Go to: Composer.
- Open: airflow-dev

Click: Open Airflow UI
- Search: flight_booking_dataproc_bq_dag

You should see the DAG.

Verify Spark file upload. Open: Cloud Storage
- Bucket: airflow-projetcs-gds-dev

Open: flight-booking-analysis -> spark-job

Verify: spark_transformation_job.py

exists.

Verify Airflow variables. In Airflow UI:

Admin -> Variables

Verify variables such as:
- env
- gcs_bucket
- bq_project
- bq_dataset
- tables

exist.

Manually run the pipeline

Inside Airflow: Find:
- flight_booking_dataproc_bq_dag

Turn it ON.
- Click: ▶ Trigger DAG

The DAG will execute:

<img width="277" height="130" alt="image" src="https://github.com/user-attachments/assets/304dec81-5391-4710-a8ad-9a01818c4a97" />

After completion, check BigQuery dataset:
- flight_data_dev

for:
- transformed_flight_data_dev
- route_insights_dev
- origin_insights_dev

These three tables are the final output of the project.

**End-to-end workflow / architecture**

<img width="549" height="358" alt="image" src="https://github.com/user-attachments/assets/47875bc0-baf1-4e68-862d-cc25511deea7" />

Final output is in BigQuery, ready for SQL analysis, dashboards, or Power BI/Tableau.



