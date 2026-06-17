I have this project Travel Booking SCD2 Merge Project.

<img width="685" height="236" alt="image" src="https://github.com/user-attachments/assets/0eec1562-7b64-4581-97fb-8d06aabb217b" />

<img width="657" height="165" alt="image" src="https://github.com/user-attachments/assets/af6c29c2-14e4-4384-be0e-325023ebd0df" />

<img width="663" height="183" alt="image" src="https://github.com/user-attachments/assets/5ce84d1f-cf65-4a1d-a8bc-352938e60c19" />

<img width="671" height="314" alt="image" src="https://github.com/user-attachments/assets/8bee424e-8824-4e77-866e-ac25126f1f5c" />

<img width="653" height="245" alt="image" src="https://github.com/user-attachments/assets/4537eed4-8712-446c-898e-a25901375d0a" />

This is one Databricks data engineering project named Travel Booking SCD2 Merge Project. It builds a Medallion pipeline: 

**CSV files → Bronze Delta tables → Data Quality → Silver SCD2 customer dimension + booking fact → SQL analytics.**

**Where to upload the files in Databricks**

Upload the project like this:

<img width="454" height="208" alt="image" src="https://github.com/user-attachments/assets/4e0ea5eb-ac0f-4e22-a810-6319bae7d51f" />

Upload the CSV files to a Unity Catalog Volume:

<img width="355" height="127" alt="image" src="https://github.com/user-attachments/assets/6d03f961-1112-4470-a5f7-dfd267e98bcf" />

Upload SQL files to Databricks SQL Editor or keep them in:

<img width="318" height="36" alt="image" src="https://github.com/user-attachments/assets/c2f8d483-a9cc-4db6-893d-fc18f7d78c9b" />

**Brief explanation of each file**

CSV files

**bookings_2025-09-23.csv** / **bookings_2025-09-24.csv**
- Daily travel booking transactions. Used to build the booking bronze table and later the booking fact table.

**customers_2025-09-23.csv** / **customers_2025-09-24.csv**
- Daily customer master data. Used to build the customer bronze table and later the SCD2 customer dimension.

**Python notebook files**

**validate_inputs.py**
- Checks parameters, arrival date, file paths, and confirms the required CSV files exist.

**10_ingest_bookings_bronze.py**
- Loads booking CSV files into the Bronze layer as raw Delta data.

**11_ingest_customers_bronze.py**
- Loads customer CSV files into the Bronze layer and prepares customer records for SCD2 logic.

**20_dq_bookings.py**
- Runs booking data quality checks: row count, required columns, non-negative amount, quantity, and discount.

**21_dq_customers.py**
- Runs customer data quality checks: required fields and email validation.

**30_customer_dim_scd2.py**
- Creates/updates the customer_dim table using SCD Type 2 logic.

**31_booking_fact_build.py**
- Builds the booking_fact table by joining bookings with the current/historical customer dimension.

**40_optimize_zorder.py**
- Optimizes Delta tables using Z-ORDER for faster queries.

**41_analyze_stats.py**
- Runs table statistics so Databricks SQL can query the tables more efficiently.

**SQL files**

**travel_booking_init.sql**
- Creates schemas/tables needed before running the pipeline.

**customer360.sql**
- Analytics query for customer-level reporting.

**daily_revenue.sql**
- Revenue reporting by day.

**data_quality_summary.sql**
- Shows data quality pass/fail summary.

**log_completion_flow.sql**
- Logs or checks pipeline completion.

**Exact Databricks GUI steps**

**Create catalog and schema**

Open Databricks.

Click Catalog on the left menu. Click Create catalog.
- Name it: **travel_bookings**. Click Create.

Open the catalog. Click Create schema.
- Name it: **default**. Click Create.

Lets explain this in detail.

**Open Databricks**

Sign in to your Databricks workspace.

You should see a screen similar to this:
- Home
- Workflows
- Catalog
- SQL Editor
- Compute
Jobs
...
  
*Click Catalog*

On the left sidebar: Catalog

(Older workspaces may show Catalog Explorer.)

*Open Catalog Explorer*

You should now see: Catalog Explorer; with existing catalogs listed.

Examples:
- main
- samples
- system

*Click Create catalog*

Look at the upper-right corner.
- Click: Create catalog

It may appear as either:
- Create catalog
- Create
- Add catalog

depending on your Databricks version.

*Enter the catalog information*

A panel appears on the right.

Fill it exactly like this:

<img width="454" height="235" alt="image" src="https://github.com/user-attachments/assets/6d0adfb8-0427-4bf5-a27c-f3833bac08a5" />

Click Create

Databricks creates the catalog.

You should now see: **travel_bookings**

listed together with:
- main
- samples
- system

*Create the Schema (**default**)*

*Open the newly created catalog*

In Catalog Explorer:
- Click: **travel_bookings**

You will see sections such as:
- Schemas
- Volumes
- Permissions
- Lineage

*Go to the Schemas section*

Under the catalog page, click: Schemas
- Click Create schema

In the upper-right corner click: Create schema (or + Create schema).

*Enter the schema details*

Fill in:

<img width="501" height="205" alt="image" src="https://github.com/user-attachments/assets/75f8760c-a7a4-4643-a71c-c6252cd5b6e0" />

Click Create

Databricks creates the schema.

What you should see afterward

Your Catalog Explorer should now look like this

<img width="330" height="53" alt="image" src="https://github.com/user-attachments/assets/f21badbc-1e14-45fe-9c20-4e5b5b558329" />

Expanding it should show:

<img width="354" height="121" alt="image" src="https://github.com/user-attachments/assets/15947f14-c098-46e7-aa02-5b34fcfcbdbc" />

*If you get an error saying "Create catalog" is missing*

This usually means one of these:
- Unity Catalog is not enabled
- You do not have permission. Ask your Databricks administrator to grant: CREATE CATALOG privileges.
- You're using Databricks Community Edition. Community Edition does not support Unity Catalog.


**Create a Volume for the CSV files**

Go to Catalog.
Open: **travel_bookings > default**

Click Create.

Choose Volume.
- Name it: **data**. Click Create.

Your base path becomes:
- /Volumes/travel_bookings/default/data

**Upload booking CSV files**

Go to Catalog.

Open: **travel_bookings > default > Volumes > data**

Click Upload to this volume.

Create/open folder: **booking_data**

Upload:
- **bookings_2025-09-23.csv**
- **bookings_2025-09-24.csv**

**Upload customer CSV files**

Stay inside the same volume: **/Volumes/travel_bookings/default/data**

Create/open folder: **customer_data**

Upload:
- **customers_2025-09-23.csv**
- **customers_2025-09-24.csv**

**Upload Python notebook files**

Click Workspace on the left.

Click your user folder.

Click Create folder.

Name it: **Travel_Booking_SCD2_Merge_Project**

Open the folder.

Create another folder:**notebooks**
- Click Import.

Upload all .py files.

Databricks will import them as notebooks.

**Upload or run SQL files**

Click SQL Editor.

Open each .sql file from your computer. Copy and paste the SQL into the editor.

First run: **travel_booking_init.sql**

IMPORTANT: This initializes the required database objects.

**Manual execution order**

Run the notebooks in this exact order:
- 1 validate_inputs.py
- 2 10_ingest_bookings_bronze.py
- 3 11_ingest_customers_bronze.py
- 4 20_dq_bookings.py
- 5 21_dq_customers.py
- 6 30_customer_dim_scd2.py
- 7 31_booking_fact_build.py
- 8 40_optimize_zorder.py
- 9 41_analyze_stats.py

Use these parameters when the notebook asks for widgets:
- arrival_date = 2025-09-24
- catalog = travel_bookings
- schema = default
- base_volume = /Volumes/travel_bookings/default/data

For the previous day test, use:
- arrival_date = 2025-09-23

Lets explain this in detail.

*Open Databricks Workspace*

Sign in to Databricks. On the left sidebar, click:
- Workspace

Navigate to your project folder:

<img width="381" height="99" alt="image" src="https://github.com/user-attachments/assets/728b945d-340c-45a2-8cfe-2af3e0012eae" />

You should see:

<img width="343" height="160" alt="image" src="https://github.com/user-attachments/assets/e4504af4-7a6f-4a8e-a6b5-c77ffc8a74f1" />

*Start or Attach a Cluster*

If you already have a running cluster, skip to Step 3.

Otherwise: Click: Compute. on the left sidebar.
- Click Create compute

Configure it. Enter:
- Name: **travel-booking-cluster**

Choose:
- Runtime: Databricks Runtime 15.x LTS

Access Mode:
- Single User

Worker Type:
- Use default

Workers:
- 1

Click Create compute

Wait until its status changes to: Running

*Run validate_inputs*

Open: **validate_inputs**

At the top of the notebook: Click:
- Connect

Choose: **travel-booking-cluster**

If widget boxes appear at the top, enter:

arrival_date
- 2025-09-24

catalog
- travel_bookings

schema
- default

base_volume
- /Volumes/travel_bookings/default/data

Click: Run all (top-right).

Wait until you see: Succeeded green checkmarks.

*Run 10_ingest_bookings_bronze*

Return to:

Workspace
- → **Travel_Booking_SCD2_Merge_Project**
- → notebooks

Open:
- **10_ingest_bookings_bronze**

Verify it is attached to: **travel-booking-cluster**

Leave the same widget values:
- arrival_date = 2025-09-24
- catalog = travel_bookings
- schema = default
- base_volume = /Volumes/travel_bookings/default/data

Click: Run all

Wait for completion.

*Run 11_ingest_customers_bronze*

Open:
- **11_ingest_customers_bronze**

Use the same widgets. Click: Run all

Wait until finished.

*Run 20_dq_bookings*

Open:
- **20_dq_bookings**

Use:
- arrival_date = 2025-09-24
- catalog = travel_bookings
- schema = default
- base_volume = /Volumes/travel_bookings/default/data

Click: Run all

Verify all DQ checks pass.

You should see no failures.

*Run 21_dq_customers*

Open:
- **21_dq_customers**

Click: Run all

Wait for completion.

Verify customer DQ checks succeed.

*Run 30_customer_dim_scd2*

Open:
- **30_customer_dim_scd2**

Click: Run all

This notebook creates or updates:
- **travel_bookings.default.customer_dim**

using SCD Type 2.

After completion, verify: Left Sidebar →

Catalog
- → **travel_bookings**
- → **default**
- → **Tables**

You should see:
- **customer_dim**

*Run 31_booking_fact_build*

Open: **31_booking_fact_build**

Click: Run all

This creates: **booking_fact**

Verify it exists:

Catalog
- → **travel_bookings**
- → **default**
- → **Tables**

You should now see:
- **customer_dim**
- **booking_fact**

*Run 40_optimize_zorder*

Open: **40_optimize_zorder**

Click: Run all

This runs:

<img width="238" height="74" alt="image" src="https://github.com/user-attachments/assets/57008269-8f95-456e-935d-f3ad5221e8c1" />

with Z-ORDER.

Wait until complete.

*Run 41_analyze_stats*

Open: **41_analyze_stats**

Click: Run all

This executes:

<img width="318" height="77" alt="image" src="https://github.com/user-attachments/assets/70192f70-159e-4f15-af4d-497ba7bbb25e" />

Wait for completion.

Verify the results Click:
- Catalog

Navigate to: travel_bookings
- → default
- → Tables

You should see tables similar to:
- bronze_bookings
- bronze_customers
- customer_dim
- booking_fact
- dq_results
- run_log

**Run the SQL analytics**

Click: SQL Editor

Open and execute the SQL files in this order:

*Customer 360*
- Paste: **customer360.sql**
- Click: Run

*Daily Revenue*
- Paste: **daily_revenue.sql**
- Click: Run

*Data Quality Summary*
- Paste: **data_quality_summary.sql**
- Click: Run

*Completion Log*
- Paste: **log_completion_flow.sql**
- Click: Run

<img width="642" height="322" alt="image" src="https://github.com/user-attachments/assets/63a761d9-9e83-4171-b225-be397e22c6d5" />




