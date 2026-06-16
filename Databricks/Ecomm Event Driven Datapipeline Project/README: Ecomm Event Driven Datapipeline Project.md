I have this project Ecomm Event Driven Datapipeline Project.

<img width="634" height="192" alt="image" src="https://github.com/user-attachments/assets/ccf190ba-77a9-42bb-a4bc-83e8f201bbf7" />

<img width="660" height="402" alt="image" src="https://github.com/user-attachments/assets/1921ec95-c37b-44d7-b4b1-b756dfc544eb" />

<img width="682" height="488" alt="image" src="https://github.com/user-attachments/assets/ee33ed8d-06c0-4650-8aae-c7bfbbcc5fc5" />

This is one project: E-commerce Event-Driven Data Pipeline using **Databricks + PySpark + Delta Lake.**

Where to upload the files in Databricks

Upload the Python files to:

**Workspace → Users → your_email → Ecomm_Event_Driven_Datapipeline → notebook/**

Upload the CSV/JSON data files to Databricks Volumes:
- /Volumes/demo-external-catalog/default/incremental_load/orders_data/source/
- /Volumes/demo-external-catalog/default/incremental_load/customers_data/source/
- /Volumes/demo-external-catalog/default/incremental_load/products_data/source/
- /Volumes/demo-external-catalog/default/incremental_load/inventory_data/source/
- /Volumes/demo-external-catalog/default/incremental_load/shipping_data/source/

Put each file in the matching folder:
- orders_*.csv       → orders_data/source/
- customers_*.csv    → customers_data/source/
- products_*.csv     → products_data/source/
- inventory_*.csv    → inventory_data/source/
- shipping_*.csv     → shipping_data/source/
- trigger_*.json     → usually a trigger/source or shared control folder

The * (asterisk) sign denotes whatever comes after "_" in or case is the different **2025_01_15** and **2025_01_16.**

**Databricks GUI steps**

**Create catalog and schema**

Open Databricks. Go to SQL Editor

Run:

<img width="458" height="80" alt="image" src="https://github.com/user-attachments/assets/21768e81-f833-4d02-9d9d-7d668daee420" />

**Create Volume folders**

Go to Catalog

Open: **demo-external-catalog → default**

Click Create. 

Select Volume

Create a volume/folder structure for:
- incremental_load/orders_data/source
- incremental_load/customers_data/source
- incremental_load/products_data/source
- incremental_load/inventory_data/source
- incremental_load/shipping_data/source

**Upload data files**

Go to Catalog

Open the correct Volume path. Click Upload to this volume

Upload each CSV file into its matching folder.

**Upload Python scripts**

Go to Workspace

<img width="634" height="140" alt="image" src="https://github.com/user-attachments/assets/d3d75a6b-a86d-4aae-a1d3-ecd27a574452" />

Open your user folder

Create folder: **Ecomm_Event_Driven_Datapipeline**

Inside it, create: notebook (this is exactly like what you see in the picture above with the folder structure)

Upload the 8 .py files from **converted_py_files.zip.**

**Run scripts manually first**

Run in this order:
- 01_orders_stage_load.py
- 02_customers_stage_load.py
- 03_products_stage_load.py
- 04_inventory_stage_load.py
- 05_shipping_stage_load.py
- 06_data_validation.py
- 07_data_enrichment.py
- 08_final_merge_operation.py

Open the first script

Double-click: **01_orders_stage_load.py**. The script editor opens.

Attach a compute cluster

At the top of the editor, you'll see:
- Connect or
- Compute

Click it.

If you already have a cluster: Select Existing Compute

Choose your cluster. Example:
- Shared Compute or
- ecommerce-cluster

Then click: Confirm

If you do NOT have a cluster:. Click: Create Compute

Configure:
- Cluster Name: ecommerce-cluster
- Runtime: Latest Databricks Runtime with Spark
- Worker Type: Smallest available
- Workers: 1
  
Click: Create Compute

Wait until the status becomes: Running 

*Run the first script*

In the upper-right corner of the notebook editor, click:
- ▶ Run All or ▶ Run

Wait until you see: Succeeded with a green check mark.

*Run the second script*

Go back to:

Workspace
- → Users
- → your_email
- → Ecomm_Event_Driven_Datapipeline
- → notebook

Open: **02_customers_stage_load.py**

Click: ▶ Run All

Wait for: Succeeded

*Repeat for the remaining scripts*

Run them one at a time in this exact order:

Script 3. Open:
- **03_products_stage_load.py**

Click: ▶ Run All

Wait for success.

Script 4. Open:
- **04_inventory_stage_load.py**

Click: ▶ Run All

Wait for success.

Script 5. Open:
- **05_shipping_stage_load.py**

Click: ▶ Run All

Wait for success.

Script 6. Open:
- **06_data_validation.py**

Click: ▶ Run All

Wait for success.

Script 7. Open:
- **07_data_enrichment.py**

Click: ▶ Run All

Wait for success.

Script 8. Open:
- **08_final_merge_operation.py**

Click: ▶ Run All

Wait until the script finishes successfully.

*What you should see after each run*

At the top of the editor:
- Running
- Running...

↓

Finished Successfully
- Succeeded ✓

If there is an issue, you'll see:
- Failed ✗

and the error message will appear in the output cells.

**Create Databricks Workflow**

Go to Workflows. Click Create Job
- Name it: Ecommerce Event Driven Pipeline

Add tasks in this order:
- orders_stage_load
- customers_stage_load
- products_stage_load
- inventory_stage_load
- shipping_stage_load
- data_validation
- data_enrichment
- final_merge_operation

Set dependencies:
- 01–05 run first
- 06 runs after 01–05 finish
- 07 runs after 06
- 08 runs after 07

Click Run now

Lets explain this in detail.

Open Workflows. In Databricks, look at the left navigation menu and click:
- Workflows

You will be taken to the Jobs page.

*Create a New Job*

In the upper-right corner, click: Create Job

A "Create Job" page opens.

Name the Workflow. Under Job name, enter:
- Ecommerce Event Driven Pipeline
 
*Add Task 1 (Orders)*

Click: Add task

Configure:
- Task name: **orders_stage_load**

Type. Select:
- Notebook

Source. Select:
- Workspace

Path

Click Browse and navigate to:

Workspace
- → Users
- → your_email
- → Ecomm_Event_Driven_Datapipeline
- → notebook
- → **01_orders_stage_load.py**

Select it.

Compute
- Choose: Existing all-purpose cluster

Select your cluster:
- ecommerce-cluster

Click: Create task

*Add Task 2 (Customers)*

Click: Add task

Configure:
- Task name: **customers_stage_load**

Notebook

Browse to: **02_customers_stage_load.py**

Compute
- ecommerce-cluster

*Set Dependency*

Under: Depends on
- Select: **orders_stage_load**

Click: Create task

*Add Task 3 (Products)*

Click: Add task

Configure:
- Task name: **products_stage_load**
- Notebook: **03_products_stage_load.py**
- Compute: ecommerce-cluster

Dependency
- Choose: **orders_stage_load**
- Create task.

*Add Task 4 (Inventory)*

Add task.
- Task name: **inventory_stage_load**
- Notebook: **04_inventory_stage_load.py**
- Compute: ecommerce-cluster

Dependency:
- Choose: **orders_stage_load**
- Create task.

*Add Task 5 (Shipping)*

Add task.
- Task name: **shipping_stage_load**
- Notebook: **05_shipping_stage_load.py**
- Compute: ecommerce-cluster

Dependency:
- Choose: **orders_stage_load**
- Create task.

*Add Task 6 (Validation)*

Click: Add task
- Task name: data_validation
- Notebook: **06_data_validation.py**
- Compute: ecommerce-cluster

Dependencies

Under Depends on, select ALL FOUR:
- customers_stage_load
- products_stage_load
- inventory_stage_load
- shipping_stage_load

Then click: Create task

*Add Task 7 (Enrichment)*

Add task.
- Task name: data_enrichment
- Notebook: **07_data_enrichment.py**
- Compute: ecommerce-cluster

Dependency:
- **data_validation**

Create task.

*Add Task 8 (Final Merge)*

Add task.
- Task name: final_merge_operation
- Notebook: **08_final_merge_operation.py**
- Compute: ecommerce-cluster

Dependency:
- **data_enrichment**

Create task.

**Review the DAG**

Your workflow should look like this:

<img width="451" height="314" alt="image" src="https://github.com/user-attachments/assets/62520aee-31c9-4504-b377-8cbc5c613ec0" />

**Save the Workflow**

Click the blue button in the upper-right corner:
- Create or Save

(depending on your Databricks version).

**Run the Workflow**

In the upper-right corner of the Job page, click:
- Run now

Databricks will start executing the tasks according to the dependencies.

**Monitor Execution**

Click the active run.

You can watch each task change status:
- Pending -> Running -> Succeeded ✓

If a task fails, it will show: Failed ✗

Click the failed task to open the logs and error output.












