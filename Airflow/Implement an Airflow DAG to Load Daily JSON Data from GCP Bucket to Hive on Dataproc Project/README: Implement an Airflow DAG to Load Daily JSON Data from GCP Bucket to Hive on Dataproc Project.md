I have the following project Implement an Airflow DAG to Load Daily JSON Data from GCP Bucket to Hive on Dataproc Project.

<img width="714" height="212" alt="image" src="https://github.com/user-attachments/assets/19833f9b-858d-44eb-86f1-3cbf4f1fbbe5" />

**Objective**: Create an Apache Airflow DAG that fetches a daily JSON file from a GCP bucket and appends the data into a Hive
table on GCP Dataproc.

**1. Airflow Setup:**
- Ensure that the necessary Airflow providers for Google Cloud Platform and Hive are installed.

**2. Airflow Connections:**
- GCP Connection: Set up a connection in the Airflow UI for accessing the GCP bucket.
- Hive Connection: Set up a connection in Airflow UI to interface with Hive on GCP Dataproc.

**3. DAG Implementation:**
- DAG Initialization: Define a DAG with a daily schedule_interval.
- Operators:
 - Use GCSToLocalFilesystemOperator to download the daily JSON file from the GCP bucket to the local Airflow directory.
 - Use HiveOperator to load the downloaded JSON data into the Hive table on Dataproc.
- Task Dependencies: Ensure the correct execution order for the tasks.

**4. Testing:**
- DAG Execution: Trigger your DAG manually and verify its successful execution.
- Data Validation: Query the Hive table on Dataproc to ensure that the data from the JSON file is correctly appended.

------------------------------------------------------------------------------------------------------------

Project name

Airflow Assignment 2: Load Daily JSON from GCS to Hive on Dataproc

The assignment is to build an Airflow DAG that downloads a daily JSON file from a GCP bucket and loads it into a Hive table on Dataproc.

<img width="655" height="195" alt="image" src="https://github.com/user-attachments/assets/b62239fb-a41a-4c3c-ab84-8acf1e2fba11" />

The DAG is named fetch_json_and_load_to_hive and uses GCSToLocalFilesystemOperator to download the JSON, then DataprocSubmitJobOperator to submit a Hive job.

**Employee.json** contains employee records with **emp_id, emp_name, dept_id,** and **salary.**

**Exact GUI steps**
Upload Employee.json to Cloud Storage

Open Google Cloud Console. Go to Cloud Storage.
- Click your bucket: **airflow_ass2**
- Click Create folder.
 - Name it:**input_files**
Open the input_files folder. Click Upload files.
- Select: **Employee.json**

Final path should be:
- gs://airflow_ass2/input_files/Employee.json

Lets explain this in detail.

Open Google Cloud Console. Open your browser. Go to:
- https://console.cloud.google.com

Sign in with your Google account. Make sure the correct project is selected at the top.

Open Cloud Storage

Click the ☰ Navigation Menu (top-left). Under Cloud Storage, click:
- Buckets

You should now see the Buckets page.

Create the Bucket (if it does not exist)

If you already see a bucket named airflow_ass2, skip to Step 4.

Otherwise:
- Click: + CREATE

For Bucket name, enter: airflow_ass2. Click Continue.

Leave the default settings: Choose where to store your data

Select: Region. Example: us-central1. Click Continue.

Choose a storage class. Leave:
- Standard

Click Continue.

Choose access control. Select:
- Uniform

Click Continue.

Protection tools
- Leave defaults.

Click: CREATE

The bucket will now appear in the bucket list.

Open the Bucket
From the Buckets page, click: **airflow_ass2**

You will enter the bucket.

You should see something similar to:
- Objects
- Permissions
- Configuration
- Lifecycle
- Monitoring

Create the Folder
- Click: CREATE FOLDER

(near the top of the Objects page)

For Folder Name, type: **input_files** Click: CREATE

You should now see:
- input_files/

inside the bucket.

**Upload Employee.json**

Click: UPLOAD FILES. File Explorer opens.

Navigate to wherever you saved: Employee.json

Here:
C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\9 Airflow\Module 6 Class 2\3 Class Assignment and Solution\Airflow_Assignment_2_Solution

Back to the GUI UPLOAD FILES.
- Select: Employee.json. Click: Open

Google Cloud will begin uploading the file.

Wait until the status changes to: Completed

**Verify the Upload**

Inside the folder, you should now see:
- Name: Employee.json

Click the file name. The details panel should show:
- gs://airflow_ass2/input_files/Employee.json

<img width="664" height="211" alt="image" src="https://github.com/user-attachments/assets/a4558899-3c18-4575-9cda-24c76a3cfbfa" />

**Upload DAG file to Cloud Composer**

Go to Composer. Click your Composer environment.

Find DAGs folder. Click the DAGs folder link.

It opens the Composer GCS bucket. Click Upload files.
- Upload: **airflow_ass2_job.py**

Lets explain this in detail.

Open Google Cloud Console

Open your browser and go to:
- https://console.cloud.google.com

Log in with the Google account that owns the Composer environment.

Open Cloud Composer

Left Navigation Menu. Click:
- ☰ Navigation Menu -> View All Products -> Under Analytics -> Click Composer

You should now see the Composer environments page.

Open Your Composer Environment

You'll see a list similar to this:

<img width="568" height="180" alt="image" src="https://github.com/user-attachments/assets/cdf570ec-4754-4009-9ec5-662b930730aa" />

Locate the DAGs Folder

Inside the environment details page, scroll down until you see: Environment configuration

There will be several tabs/sections. Find: DAGs folder

It looks similar to:
- gs://us-central1-composer-env-xxxxxx-bucket/dags

Next to it is a blue link. Click the DAGs folder link.

Composer Opens the GCS Bucket

You are automatically redirected to Cloud Storage.

The page title usually looks like:
- Cloud Storage
- Bucket details

You should now be inside a folder called:
- dags/

Example path:
- composer-env-bucket -> dags/

Upload the DAG File

At the top of the page, click: UPLOAD FILES

(Blue button near the top.)

A Windows File Explorer window opens.

Select the DAG File

Navigate to the folder where you saved the DAG.

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\9 Airflow\Module 6 Class 2\3 Class Assignment and Solution\Airflow_Assignment_2_Solution

Select: **airflow_ass2_job.py**

Click: Open

Wait for Upload Completion

You'll see a progress indicator.

After it finishes, you should see:

<img width="251" height="60" alt="image" src="https://github.com/user-attachments/assets/7587880e-18d1-41d7-9006-b6252a60442b" />

Verify Composer Detects the DAG

Go back to Composer:

Navigation Menu
- → Composer
- → composer-env

Click: Open Airflow UI

Airflow opens in a new tab.

Check the DAG in Airflow

In the Airflow UI: Use the search box and type:
- fetch_json_and_load_to_hive

This is the DAG ID defined in your file:

dag = DAG(
    'fetch_json_and_load_to_hive',
    ...
)

You should now see:

DAG ID
- fetch_json_and_load_to_hive

with a toggle switch.

In our airflow_ass2_job.py file it looks like:

<img width="783" height="357" alt="image" src="https://github.com/user-attachments/assets/ac1d1cbc-a7fb-45fc-bee2-7134ac29df01" />

Enable the DAG

Turn the toggle from: Off to On

The DAG is now deployed in Composer.

What you should have after this step

<img width="462" height="226" alt="image" src="https://github.com/user-attachments/assets/b016fdb5-d2eb-4aaa-b13b-25617e807722" />

**Create / verify Airflow GCP connection**

In Airflow UI, go to Admin. Click Connections.

Search for: **google_cloud_default**

If it exists, leave it. If not, click + Add Connection.

Use:
- Connection Id: google_cloud_default
- Connection Type: Google Cloud

Save.

Lets explain this in detail.

Open Cloud Composer

Go to:  https://console.cloud.google.com

Then click: ☰ Navigation Menu -> Composer

You will see your Composer environments.

Example:

<img width="534" height="78" alt="image" src="https://github.com/user-attachments/assets/4579a2e0-399d-47ac-9113-4332a0044094" />

Open Airflow UI

Inside the Composer environment page, locate the button near the top right: Open Airflow UI. Click it.

A new browser tab opens showing the Airflow web interface.

Open the Admin Menu

At the top of the Airflow page, you'll see a menu bar similar to:
- DAGs    Browse    Docs    Admin    Security

Click: Admin. A dropdown menu appears.

Open Connections

From the Admin dropdown, click: Connections

Example:

<img width="630" height="146" alt="image" src="https://github.com/user-attachments/assets/2ed34587-8584-45bc-a11f-e006eb4b8e9c" />

Search for the Connection

Near the upper-right corner of the Connections page, find the search box labeled: Search

Click inside it and type: google_cloud_default

Press: Enter

Check if the Connection Exists. You may see a row like this:

<img width="678" height="326" alt="image" src="https://github.com/user-attachments/assets/8c88424f-f594-4847-a555-9b51537523ab" />

Lets check the python file.













