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





