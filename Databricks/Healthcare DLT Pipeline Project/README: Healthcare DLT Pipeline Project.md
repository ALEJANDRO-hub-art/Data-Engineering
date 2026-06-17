I have this project Healthcare DLT Pipeline Project.

<img width="635" height="196" alt="image" src="https://github.com/user-attachments/assets/e752015e-e5d3-4e94-890d-21158ac3ae1d" />

<img width="655" height="213" alt="image" src="https://github.com/user-attachments/assets/7b06bd4a-bd38-4a0b-b4e0-1896de3a2ccb" />

<img width="624" height="232" alt="image" src="https://github.com/user-attachments/assets/16850d4c-b3a3-4243-a90f-6abaf29ccd12" />

Project name: Healthcare DLT Pipeline Project

It is one Databricks project using **Delta Live Tables** and the **Bronze → Silver → Gold** architecture. The README says the project processes patient admission data with streaming, data quality rules, enrichment, and analytics.

**Where to upload each file**

Upload CSV files here

Upload these 4 CSV files into a Databricks Unity Catalog Volume:
- **/Volumes/gds_de_bootcamp_new/default/healthcare_data/**

Files:
- diagnosis_mapping.csv
- patients_daily_file_1_2025.csv
- patients_daily_file_2_2025.csv
- patients_daily_file_3_2025.csv

The **feed_raw_tables.py** file reads from that exact Volume path **and writes Delta tables named:**
- gds_de_bootcamp_new.default.raw_diagnosis_map
- gds_de_bootcamp_new.default.raw_patients_daily

**Upload notebook/script files here**

Upload these to Databricks Workspace → your project folder:
- **feed_raw_tables.py**
- **healthcare_dlt_processing.py**
- **README.md**

Important: **feed_raw_tables.py** is a Python notebook.
**healthcare_dlt_processing.py** contains SQL DLT code, so create/import it **as a SQL notebook**, not a normal Python notebook.

<img width="656" height="410" alt="image" src="https://github.com/user-attachments/assets/ae276015-f760-4599-bf85-6799701eb47b" />

**Exact GUI steps in Databricks**

**Create catalog, schema, and volume**

Open Databricks. Left menu → Catalog. Click Create catalog.
- Catalog name: **gds_de_bootcamp_new**. Click Create.

Open the catalog: **gds_de_bootcamp_new**. Click Create schema.
- Schema name: **default**. Click Create.

Inside **gds_de_bootcamp_new.default**, click Create → Volume.
- Volume name: **healthcare_data**. Click Create.

**Upload the CSV files to the Volume**

Left menu → Catalog. Open:
- gds_de_bootcamp_new → default → Volumes → healthcare_data

Click Upload to this volume. Upload:
- diagnosis_mapping.csv
- patients_daily_file_1_2025.csv
- patients_daily_file_2_2025.csv
- patients_daily_file_3_2025.csv

Final path should be:
- /Volumes/gds_de_bootcamp_new/default/healthcare_data/

**Upload/import the notebooks**

Left menu → Workspace. Click your user folder. 

Click Create → Folder.
- Name it: **Healthcare_DLT_Pipeline_Project**

Open the folder. Click Import.
- Upload: **feed_raw_tables.py**

For **healthcare_dlt_processing.py**, create a new SQL notebook:

Click Create → Notebook
- Name: healthcare_dlt_processing
- Language: SQL
 
Paste the DLT SQL code from healthcare_dlt_processing.py.

**Run the raw ingestion notebook**

Open: **feed_raw_tables.py**

Attach a cluster. Run the first cell to load:

This creates:
- **gds_de_bootcamp_new.default.raw_diagnosis_map**

For patient files, the notebook currently points to only one file at a time. It has file 1 and file 2 commented out, and file 3 active.

Run it 3 times by changing the path each time:

<img width="520" height="66" alt="image" src="https://github.com/user-attachments/assets/48145107-61ed-4ad7-af3c-165afa0d3671" />

Then:

<img width="511" height="66" alt="image" src="https://github.com/user-attachments/assets/cd80a8e2-00b0-44e2-80c5-1f994befdecb" />

Then:

<img width="510" height="66" alt="image" src="https://github.com/user-attachments/assets/739832e8-9bce-44c1-b7f8-55dd0c900f18" />

This creates/appends to:
- **gds_de_bootcamp_new.default.raw_patients_daily**

Lets explain this in detail.

**Run the Raw Ingestion Notebook (feed_raw_tables.py)**

This step loads the CSV files from your Unity Catalog Volume into Delta tables. The notebook reads:
- diagnosis_mapping.csv → **raw_diagnosis_map**
- patients_daily_file_1_2025.csv
- patients_daily_file_2_2025.csv
- patients_daily_file_3_2025.csv

and appends patient records into **raw_patients_daily**.

Go to:
- Databricks then
- Workspace then
- Locate the notebook (Navigate to the folder where you uploaded: **feed_raw_tables.py**)
 - Click: **feed_raw_tables.py**. The notebook opens in the editor.

Lets create a CLuster.

I didnt create a cluster. Lets explain how to do it.

*Step 1: Open Compute*

In the Databricks left menu: Compute. Click it.

*Step 2: Create a New Cluster*

In the upper-right corner click: Create Compute

(or Create Cluster, depending on your Databricks version)

*Step 3: Configure the Cluster*

Fill in:
- Compute Name: healthcare-cluster
- Compute Policy. Select: Unrestricted (if available)
- Access Mode. Select: Single User

This is the safest option for the project.

Databricks Runtime Version
- Select: 14.3 LTS or any recent runtime: 13.3 LTS+

Photon
- Leave: Enabled

Worker Type
- Choose a small machine. Example: Standard_DS3_v2 or i3.xlarge

depending on cloud provider.

Workers
- Set: 1

This project is tiny and only loads CSV files.

*Step 4: Create the Cluster*

Scroll to the bottom. Click:
- Create Compute

*Step 5: Wait for Startup*

Databricks now starts the cluster.

Status changes: Pending -> Starting -> Running

This usually takes: 2–5 minutes

*Step 6: Open the Notebook*

Go to: Workspace
- Open: **feed_raw_tables.py**

*Step 7: Attach the Cluster*

At the top-right of the notebook click: Connect or Select Compute

You should now see: healthcare-cluster. Select it.

Wait until the notebook shows: Connected

*Attach a Cluster*

Locate the cluster selector. Top-right corner of the notebook.

You will see: Connect or Select Compute

Select the cluster created before

Example: **healthcare-cluster**

Wait until status becomes: Running

**Create the Delta Live Tables pipeline**

Left menu → Workflows. Click Delta Live Tables. Click Create pipeline.
- Pipeline name: **healthcare_dlt_pipeline**
- Product edition: choose Advanced if available.
- Pipeline mode: choose Triggered.
- Source code: select the SQL notebook:
 - /Workspace/.../Healthcare_DLT_Pipeline_Project/healthcare_dlt_processing
- Target catalog: **gds_de_bootcamp_new**
- Target schema: default

Click Create.

**Start the pipeline**

Open the pipeline: **healthcare_dlt_pipeline**. Click Start.

Wait for the graph to finish.

Check that these tables are created:
- Bronze:
  - diagnostic_mapping
  - daily_patients
- Silver:
  - processed_patient_data
- Gold:
 - patient_statistics_by_admission_date
 - patient_statistics_by_diagnosis
 - patient_statistics_by_gender

The DLT file creates those bronze, silver, and gold tables with data quality constraints.


Lets where this Bronze, Silver and Gold steps are and what do they do: Lets inspect **healthcare_dlt_processing.py** file:

In here we do:
- BRONZE LAYER: DIAGNOSTIC MAPPING
- BRONZE LAYER: DAILY PATIENTS (STREAMING)
- SILVER LAYER: PROCESSED PATIENT DATA
- GOLD LAYER: PATIENT STATISTICS BY ADMISSION DATE
- GOLD LAYER: PATIENT STATISTICS BY DIAGNOSIS
- GOLD LAYER: PATIENT STATISTICS BY GENDER

**View results**

Left menu → Catalog.
Open: **gds_de_bootcamp_new → default → Tables**

Open the gold tables:
- patient_statistics_by_admission_date
- patient_statistics_by_diagnosis
- patient_statistics_by_gender

Click Sample Data to preview results.

**End-to-end workflow / architecture**

<img width="489" height="478" alt="image" src="https://github.com/user-attachments/assets/1a25f39c-dfea-4750-8e7a-bfbfb2e20053" />

Final result: raw patient CSVs are loaded into Delta tables, cleaned with DLT quality rules, joined with diagnosis descriptions, and aggregated into gold analytics tables for healthcare reporting.










