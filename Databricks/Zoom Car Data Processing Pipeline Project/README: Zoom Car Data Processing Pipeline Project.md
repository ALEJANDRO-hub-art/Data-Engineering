I have this project Zoom Car Data Processing Pipeline Project. 

<img width="651" height="295" alt="image" src="https://github.com/user-attachments/assets/669526a6-fae8-4ae8-ac11-ac87f4e1d4cd" />

<img width="683" height="199" alt="image" src="https://github.com/user-attachments/assets/40fd7a7c-7e20-4001-85d3-068f1123915d" />

<img width="642" height="196" alt="image" src="https://github.com/user-attachments/assets/0c90034a-d6d0-49be-9eb3-e3373f462f72" />

<img width="634" height="159" alt="image" src="https://github.com/user-attachments/assets/0b959afa-c4c2-42f5-8b21-0258de7d06a6" />

<img width="650" height="192" alt="image" src="https://github.com/user-attachments/assets/69509955-5dc4-45fc-a7a8-3b326c08af8d" />

<img width="643" height="144" alt="image" src="https://github.com/user-attachments/assets/ebf2ee85-16f4-469d-8526-0c4adc431181" />


This is one Databricks project: Zoom Car Data Processing Pipeline. The assignment requires daily booking (**zoom_car_bookings_20240720,1 and 2**) /customer (**zoom_car_customers_20240720,1 and 2**)  JSON files, two processing notebooks (**01_process_zoom_car_bookings.py and 02_process_zoom_car_customers.py**), one merge notebook (**03_merge_zoom_car_data.py**), and a Databricks job workflow (**databricks_job_flow.json**).

What each file/folder does

**data/bookings/**

Stores daily booking JSON files like:
- **zoom_car_bookings_20240720.json**
- **zoom_car_bookings_20240721.json**
- **zoom_car_bookings_20240722.json**

These contain booking records with booking ID, customer ID, car ID, date, start/end time, amount, and status.

**data/customers/**

Stores daily customer JSON files like:
- **zoom_car_customers_20240720.json**
- **zoom_car_customers_20240721.json**
- **zoom_car_customers_20240722.json**

These contain customer ID, name, email, phone, signup date, and status.

notebooks / .py files

Upload these to Databricks as notebooks:

- **01_process_zoom_car_bookings.py**

Cleans booking data, validates dates/status, calculates duration, and writes to **staging_bookings_delta.**

- **02_process_zoom_car_customers.py**

Cleans customer data, validates emails/status, normalizes phone numbers, calculates tenure, and writes to **staging_customers_delta.**

- **03_merge_zoom_car_data.py**

Reads both staging tables, merges into target Delta tables, updates existing records, inserts new records, and deletes cancelled bookings.

- **sql/create_schema.sql**

Creates the catalog/schema used by the notebooks.

- **jobs/databricks_job_flow.json**

Defines the Databricks workflow with three tasks: process bookings, process customers, then merge data.

- **README.md**

Explains upload locations, execution order, expected tables, and the daily parameter format.


**Where to upload the files in Databricks**

Use this structure:

Workspace:
- /Workspace/Shared/zoom_car_project/notebooks/

Volumes:
- /Volumes/main/zoom_car_db/raw/bookings/
- /Volumes/main/zoom_car_db/raw/customers/

Upload these files here:
- 01_process_zoom_car_bookings.py
- 02_process_zoom_car_customers.py
- 03_merge_zoom_car_data.py

to:
- /Workspace/Shared/zoom_car_project/notebooks/

Upload booking JSON files to:
- /Volumes/main/zoom_car_db/raw/bookings/

Upload customer JSON files to:
- /Volumes/main/zoom_car_db/raw/customers/

This matches the README upload locations.

**Create catalog/schema**

Open Databricks. Go to Catalog on the left menu. Click your catalog, usually **main**.

Click Create schema.
- Name it: **zoom_car_db**. Click Create.

Final schema:
- **main.zoom_car_db**

**Create folders in Volume**

Go to Catalog. Open:
- **main**

Open schema:
- **zoom_car_db**. Click Create.

Choose Volume.
- Name it: **raw**. Open the volume.

Create two folders:
- **bookings**
- **customers**

Final paths:
- /Volumes/main/zoom_car_db/raw/**bookings/**
- /Volumes/main/zoom_car_db/raw/**customers/**

**Upload JSON files**

Upload booking files here:
- **/Volumes/main/zoom_car_db/raw/bookings/**

Files:
- **zoom_car_bookings_20240720.json**
- **zoom_car_bookings_20240721.json**
- **zoom_car_bookings_20240722.json**

Upload customer files here:
- /Volumes/main/zoom_car_db/raw/**customers**/

Files:
- **zoom_car_customers_20240720.json**
- **zoom_car_customers_20240721.json**
- **zoom_car_customers_20240722.json**

**Upload notebooks**

Go to Workspace. Click Shared.
- Create folder: **zoom_car_project**

Inside it, create folder:
- notebooks. Click Import.

Upload these .py files:
- **01_process_zoom_car_bookings.py**
- **02_process_zoom_car_customers.py**
- **03_merge_zoom_car_data.py**

Final location:
- **/Workspace/Shared/zoom_car_project/notebooks/**

**Create or attach cluster**

Go to Compute. Click Create compute.
- Name it: **zoom-car-cluster**

Use a DBR version that supports Delta Lake. Click Create compute.

Wait until the cluster is Running.

Lets explain this in detail.

*1. Open Compute*

Log in to Databricks.

On the left sidebar, click: Compute

(Older Databricks versions may show Clusters instead of Compute.)

*2. Create New Compute*
- In the top-right corner click: Create compute

You will be taken to the cluster creation page.

*3. Configure the Cluster*

*Compute Name*

In the Compute name field enter: **zoom-car-cluster**

*Policy*

Leave:
- Unrestricted

(if your workspace allows it)

*Cluster Mode*
- Select: Single Node

This project is small and does not require multiple workers.

*Databricks Runtime Version*

Click the Databricks Runtime Version dropdown. Select a runtime that includes Delta Lake, for example:
- 15.4 LTS (Spark 3.5.x, Scala 2.12) or any newer LTS runtime available.

*Node Type*

Leave the default selected by Databricks.

Typical examples:
- Standard_DS3_v2 or i3.xlarge

depending on your cloud provider.

*Workers*

If using Single Node:
- 0 Workers

Databricks will configure this automatically.

*4. Expand Advanced Options*
- Click: Advanced Options

You do not need to change anything for this assignment.

Leave defaults.

*5. Create Cluster*
- Click the blue button: Create compute

*6. Wait for Startup*

You will return to the Compute page.

Status will change: Pending -> Starting -> Running

Wait until you see: 🟢 Running

**Copy the Cluster ID**

You will need this for:
- databricks_job_flow.json
- 
Click your cluster: **zoom-car-cluster**

Look at the browser URL.

Example:
- https://adb-1234567890123456.7.azuredatabricks.net/compute/clusters/**0518-153015-abcd123**

The Cluster ID is:
- **0518-153015-abcd123**

Open: **jobs/databricks_job_flow.json**
- Replace: "<YOUR_CLUSTER_ID>" with: "**0518-153015-abcd123**"

**Attach Notebook to Cluster**

For each notebook:
- **01_process_zoom_car_bookings**
- **02_process_zoom_car_customers**
- **03_merge_zoom_car_data**

Open the notebook in Workspace. At the top-left click the Compute dropdown.
Select: **zoom-car-cluster**

Wait for: 'Connected' to appear.

Now the notebook is ready to run.

Lets explain this in detail.

**Attach a Notebook to the Cluster**

You must do this for all 3 notebooks:
- **01_process_zoom_car_bookings**
- **02_process_zoom_car_customers**
- **03_merge_zoom_car_data**

*Step 1: Open Workspace*

In Databricks, click Workspace on the left menu.

Navigate to:

<img width="337" height="88" alt="image" src="https://github.com/user-attachments/assets/abeb7dfb-415f-4e5e-9050-afb8174e20f3" />

You should see:
- **01_process_zoom_car_bookings**
- **02_process_zoom_car_customers**
- **03_merge_zoom_car_data**

*Step 2: Open the First Notebook*

- Click: **01_process_zoom_car_bookings**

The notebook opens in a new tab.

*Step 3: Locate the Compute Selector*

Look at the top of the notebook page. Near the upper-left area you will see one of these:
- Connect or Select Compute or Detached

or a dropdown showing a cluster name. Click it.

*Step 4: Select Your Cluster*

A dropdown appears. Under Running Compute select:
- zoom-car-cluster

Click it.

*Step 5: Wait for Attachment*

Databricks will attach the notebook to the cluster.

You may see: Attaching... or Connecting...

Wait 10–30 seconds.

When complete you will see: **Connected or zoom-car-cluster**

displayed in the notebook header.

*Step 6 Verify Connection*

Look at the upper-right corner of the notebook. You should see: 
- 🟢 Running and
- zoom-car-cluster

If you see:
- Detached. The notebook is not attached yet.

*Step 7: Repeat for Notebook #2*

Return to:

Workspace
- → Shared
- → zoom_car_project
- → notebooks

Open:
- **02_process_zoom_car_customers**

Repeat:
- Click Connect / Select Compute

Choose: **zoom-car-cluster**

Wait until connected.

*Step 8: Repeat for Notebook #3*

Open:
- **03_merge_zoom_car_data**

Repeat:
- Click Connect / Select Compute

Select: **zoom-car-cluster**

Wait for connection.

*Step 9: Confirm All Notebooks Are Attached*

Open each notebook and verify the top bar shows:
- zoom-car-cluster; instead of: Detached

At this point all notebooks are attached and ready to run.

Next Step

Run the notebooks in this exact order:
- **1 01_process_zoom_car_bookings**
- **2 02_process_zoom_car_customers**
- **3 03_merge_zoom_car_data**

using:
- **process_date = 20240720**

for the first test run.

Lets explain this in detail.

**Exact GUI Steps: Run Notebook #1 (Bookings)**

*Step 1: Open the Notebook*

In Databricks click Workspace.

Navigate to:

<img width="338" height="94" alt="image" src="https://github.com/user-attachments/assets/cbe03f19-8dc7-4d0c-b386-6e46bbb3d89b" />

Double-click:
- **01_process_zoom_car_bookings**

*Step 2: Verify Cluster Connection*

At the top of the notebook verify you see: **zoom-car-cluster**

If you see Detached, click it and select: **zoom-car-cluster**

Wait until it shows: Connected

*Step 3: Set the Parameter*

At the top of the notebook locate:

<img width="388" height="82" alt="image" src="https://github.com/user-attachments/assets/bac6199c-c9ed-4ea7-a827-4c875159020d" />

or the Databricks widget box.

Enter: 20240720

*Step 4: Run the Notebook*

Click the top-right button:
- Run All or ▶ Run All

Wait until all cells have green checkmarks.

*Step 5: Verify Results*

Click: Catalog

Navigate to:

<img width="200" height="66" alt="image" src="https://github.com/user-attachments/assets/c9ef7d39-25d5-4b09-8ba7-adeadc5a0b3f" />

Verify table exists: **staging_bookings_delta**

**Exact GUI Steps: Run Notebook #2 (Customers)**

*Step 1*

Open:
- **02_process_zoom_car_customers**

*Step 2*

Verify cluster: **zoom-car-cluster** is attached.

*Step 3*

Set:
- process_date = 20240720

*Step 4*

Click: Run All

Wait for completion.

*Step 5*

Go to:

<img width="219" height="71" alt="image" src="https://github.com/user-attachments/assets/40b46d70-8a59-4874-a1cd-2c935639200c" />

Verify table exists:
- **staging_customers_delta**

**Exact GUI Steps: Run Notebook #3 (Merge)**

*Step 1*

Open:
- **03_merge_zoom_car_data**

*Step 2*

Verify cluster: **zoom-car-cluster** is attached.

*Step 3*

Set: process_date = 20240720

*Step 4*

Click: Run All

Wait until the notebook finishes.

The notebook will:
- Read staging_bookings_delta
- Read staging_customers_delta
- Merge records into target tables
- Delete cancelled bookings
- Create a final joined view

**View the Final Data**

Click: Catalog

Open:

<img width="151" height="52" alt="image" src="https://github.com/user-attachments/assets/632b2353-acf0-4257-829c-d868755ab37f" />

Click: **target_bookings_delta**
Click: **Preview**

You should see booking records loaded from:
- **zoom_car_bookings_20240720.json**

Open: **target_customers_delta**
- Click: Preview

You should see customer records loaded from:
- **zoom_car_customers_20240720.json**

**Expected First Test Run Result**

Input files:
- **zoom_car_bookings_20240720.json**
- **zoom_car_customers_20240720.json**

Processing:

<img width="459" height="242" alt="image" src="https://github.com/user-attachments/assets/8c50ab8e-3c0b-40a7-b289-e3599dcb0373" />

After all three notebooks complete successfully, the assignment execution is finished and ready for creating the Databricks Workflow job.













