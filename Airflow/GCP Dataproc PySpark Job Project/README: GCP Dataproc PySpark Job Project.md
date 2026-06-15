I have this project GCP Dataproc PySpark Job Project.

<img width="760" height="255" alt="image" src="https://github.com/user-attachments/assets/f3622321-1ef2-4d3b-99c9-d9031979d943" />

**Objective**: Automate a workflow using Apache Airflow to process daily incoming CSV files from a GCP bucket using a Dataproc PySpark job and save the transformed data into a Hive table.

**Tasks:**

1. Setup:
- Create a Google Cloud Platform (GCP) bucket to store the daily CSV files.
- Set up an Apache Airflow environment and ensure GCP and Dataproc plugins/hooks are available.

2. DAG Configuration:
- Create a new DAG gcp_dataproc_pyspark_dag.
- Schedule the DAG to run once a day.
- Ensure catchup is set to False: catchup=False.

3. File Sensor Task:
- Add a GCSObjectExistenceSensor task to check for the presence of the daily CSV file in the GCP bucket.
- Configure the task to poke for the file every 5 minutes for a maximum of 12 hours.

4. Dataproc Cluster Creation Task:
- Use the DataprocClusterCreateOperator to create a new Dataproc cluster.
- Define and configure the cluster specifications as needed.

5. PySpark Job Execution Task:
- Upload your PySpark script to GCP (either in a bucket or Cloud Storage).
- Use the DataProcPySparkOperator to execute the PySpark script on the created Dataproc cluster.
- The PySpark script should:
 - Read the daily CSV file from the GCP bucket.
 - Perform some logical transformations on the data.
 - Write the transformed data into a Hive table.

6. Dataproc Cluster Deletion Task:
- Use the DataprocClusterDeleteOperator to delete the Dataproc cluster once the PySpark job is successfully completed.

7. DAG Dependency Configuration:
- Set the task dependencies using the set_upstream and set_downstream methods or the bitshift operators (>> and <<).
- Ensure that the DAG tasks run in the correct sequence.

Evaluation Criteria:
- Proper configuration and structuring of the Airflow DAG.
- Successful execution and scheduling of the DAG.
- Correct sensing of the daily CSV file.
- Successful creation and deletion of the Dataproc cluster.
- Successful execution of the PySpark job with the desired transformation.
- Proper writing of the transformed data to the Hive table.

Tips:
- Remember to configure the necessary GCP connection in the Airflow web UI.
- Ensure you handle exceptions and potential issues in the workflow, such as cluster creation failures or script execution errors.
- Log important steps and outputs for easier debugging.

----------------------------------------------------------------------------------------------------------------------------------

Project name

Airflow Assignment: GCP Dataproc PySpark Job

The goal is to use Airflow/Cloud Composer to detect a daily CSV in GCS, create a Dataproc Spark cluster, run a PySpark job, write filtered results into a Hive table, then delete the cluster.

<img width="726" height="344" alt="image" src="https://github.com/user-attachments/assets/04ea9236-e61c-444e-8aa9-739a8935a52e" />

GCS bucket structure

Create this bucket/folder structure:

<img width="336" height="118" alt="image" src="https://github.com/user-attachments/assets/7e92d355-2f03-491a-a5c3-96bdc5200d37" />

Important: your DAG expects:

<img width="298" height="53" alt="image" src="https://github.com/user-attachments/assets/c102b2c9-7bc2-45fa-bf1f-88f0d528a6ff" />

**Exact GUI steps in Google Cloud**

Create the GCS bucket

Open Google Cloud Console. Search Cloud Storage
Click Buckets. Click Create

- Bucket name:airflow_ass1
- Region: choose: us-central1

Click Create

Create folders in the bucket

Open bucket: airflow_ass1. Click Create folder
- Create: input_files
- Create another folder: python_file
- Create another folder: hive_data

Upload the CSV file

Open bucket: airflow_ass1

Open folder: input_files

Click Upload files. Select employee(1).csv. Rename it in GCS to: employee.csv

Final path must be:
- gs://airflow_ass1/input_files/employee.csv

Upload the PySpark file.

Open bucket: airflow_ass1. Open folder: python_file

Click Upload files

Upload: employee_batch.py

Final path must be:
- gs://airflow_ass1/python_file/employee_batch.py

**Cloud Composer / Airflow GUI steps**

Create Composer environment

In Google Cloud Console, search Composer. Click Cloud Composer. Click Create environment
- Choose Composer 2 or Composer 3
- Name: airflow-assignment-env
- Region: us-central1

Service account: use one with permissions for:
- Cloud Storage
- Dataproc
- Composer
- BigQuery optional, not required here

Click Create

Lets explain this in detail.

Search for Composer

At the top search bar: Type: Composer. Then click: **Cloud Composer**

under the results.

Enable the API (if prompted)

If this is your first Composer environment, you may see:

- Enable Cloud Composer API. Click: ENABLE

Wait a few minutes until the API is enabled.

Click Create Environment

Inside Cloud Composer: Top of the page: Click:
- + CREATE ENVIRONMENT

You may see options such as:
- Composer 3
- Composer 2

Select:
- Composer 3

(Recommended)

If Composer 3 is unavailable in your region, choose Composer 2.

Configure Basic Information

Under Environment configuration, fill in:

- Name. Enter: **airflow-assignment-env**
- Region. Open the dropdown. Select: us-central1 (Iowa)

Select the Service Account

Scroll down to the section called: Node configuration or Environment configuration

Locate: Service account. Click the dropdown. Select the service account you created earlier.

Example:
- composer-sa@your-project-id.iam.gserviceaccount.com

Verify Required Permissions. The service account should have these IAM roles:
- ✓ Cloud Composer Worker
- ✓ Storage Admin
- ✓ Dataproc Editor (Optional)
- ✓ BigQuery User

To verify: Open another tab. Go to:

Navigation Menu
- → IAM & Admin
- → IAM

Find your service account. Confirm these roles exist.

If not:
- Click the pencil icon.
- Click Add Another Role. Add the missing role.
- Click Save.

Return to Composer.

Leave Remaining Settings as Default

Unless your assignment specifies otherwise: Leave these unchanged:
- Image Version: Use the default Composer image. Example:
 - composer-3-airflow-2.x
- Networking. Keep: Default network
- Environment Size. Keep: Small
- Airflow Database. Keep default.
- Encryption. Keep: Google-managed encryption key

Create the Environment

Scroll to the bottom.
- Click: CREATE

Wait for Provisioning

Composer will now create:
- GKE cluster
- Airflow instance
- Cloud Storage bucket
- Airflow database

This process typically takes: 20–40 minutes

The status changes from: Creating to Running

Open the Airflow GUI

Once the status becomes Running:
- Click the name: **airflow-assignment-env**

Then click: OPEN AIRFLOW UI

You will be redirected to the Airflow web interface where you can upload DAGs and run your assignment.

<img width="648" height="348" alt="image" src="https://github.com/user-attachments/assets/d2ad6b81-fe13-4bf2-bab5-12a1c2927dfb" />

After this step, you'll be ready to upload your DAG files into the Composer environment and execute the Airflow assignment from the Airflow GUI.

**Upload the DAG file**

Open Cloud Composer. Click your environment:
- airflow-assignment-env

Find DAGs folder. Click the DAGs bucket link

Open folder: dags/
- Click Upload files. Upload: **airflow_ass1_job.py**

The DAG should appear in Airflow as: **gcp_dataproc_spark_job**

**Open Airflow UI**

Go back to Cloud Composer. Open your environment
- Click Airflow UI

Search for DAG: **gcp_dataproc_spark_job**

Toggle it ON

Click the DAG name

Click Trigger DAG

**DAG execution flow**

Your DAG runs in this order:

<img width="302" height="138" alt="image" src="https://github.com/user-attachments/assets/11d88e1c-2ecf-40ef-afe6-0d9ea2dfca99" />


Explanation:

file_sensor_task checks if this file exists:
- gs://airflow_ass1/input_files/employee.csv

create_cluster creates a temporary Dataproc cluster named: airflow-cluster

submit_pyspark_job runs:
- gs://airflow_ass1/python_file/employee_batch.py

delete_cluster deletes the Dataproc cluster after the Spark job finishes.

<img width="571" height="405" alt="image" src="https://github.com/user-attachments/assets/f21ffa41-e935-400e-b339-5dc3329835c9" />

**Expected output**

The PySpark job keeps only employees with:

- salary >= 60000

So the Hive table should contain employees like Alice, Charlie, and Eve from your sample CSV.













