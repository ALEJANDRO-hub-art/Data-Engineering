I have this project UPI Transactions CDC Feed Project.

<img width="676" height="216" alt="image" src="https://github.com/user-attachments/assets/d49e1515-a27c-4535-a781-d38e3f35b24e" />

<img width="636" height="214" alt="image" src="https://github.com/user-attachments/assets/00608f03-c5bd-41fe-bf18-2244fa9cbdea" />

This is one Databricks project called UPI Transactions CDC Feed Project. It builds a real-time CDC pipeline using Databricks + Delta Lake + Spark Structured Streaming + Unity Catalog. 

The flow is: **mock UPI transaction data → CDC-enabled Delta table → streaming pipeline → merchant aggregation table.**

<img width="719" height="382" alt="image" src="https://github.com/user-attachments/assets/fdcb55aa-672f-4fff-b1f8-1dfc97e94cea" />

Where to upload the files

Upload all .py files into Databricks Workspace, not DBFS.

Recommended folder:

<img width="426" height="185" alt="image" src="https://github.com/user-attachments/assets/f42c1ac7-4ca9-4106-ad58-45b71464d5b4" />

No CSV files are needed because the mock data generator creates the transaction data.

**Exact Databricks GUI steps**

**Create project folder**

*Open Databricks*
- Click Workspace
- Open Users
- Click your user email
- Click Create
- Click Folder. Name it: **UPI_Transactions_CDC_Project**
- Click Create

**Upload the Python files**
Open the folder **UPI_Transactions_CDC_Project**
- Click Create
- Click File

Upload these files one by one:
- 01_enhanced_data_model(2).py
- 02_realtime_streaming_pipeline(2).py
- 03_enhanced_mock_data_generator(2).py
- test.py
- README.md

**Create or attach a cluster**

Click Compute. Click Create compute
- Name it: **upi-cdc-cluster**

Choose a Databricks Runtime that supports Delta Lake and Structured Streaming. Use a single-node cluster if this is for class/testing
- Click Create compute

Wait until the cluster status says Running

Lets explain this in detail.

Based on your UPI CDC Streaming Project files, the cluster only needs to support **Delta Lake, Structured Streaming, and Change Data Feed (CDF)**. The README specifically recommends Databricks **Runtime 13.3 LTS or later.**

*Create or Attach a Cluster (Exact Databricks GUI Steps)* Choose Option A or B

**Option A (Recommended)**: Create a New Cluster*

Open Databricks Workspace

After logging in: Look at the left sidebar. Click Compute

You should see a page similar to: 

<img width="266" height="94" alt="image" src="https://github.com/user-attachments/assets/a585878b-86e2-4d19-b445-f869fdb9f9cf" />

*Click Create Compute*

Top-right corner: + Create Compute. Click it.

*Configure the Cluster*

Fill in the fields exactly:

<img width="530" height="394" alt="image" src="https://github.com/user-attachments/assets/1c883169-e60f-4464-a9bd-469e74d4f7a2" />

*Expand Advanced Options*

Click: Advanced Options. Then: Spark

Leave everything as default.

No special libraries are required because:
- Delta Lake is built into Databricks Runtime
- Structured Streaming is built in
- CDC support is built in

The project code already uses:

<img width="391" height="102" alt="image" src="https://github.com/user-attachments/assets/6dcf5613-4020-4e05-9507-68efe8d9c315" />

which works natively in Databricks Runtime.

*Click Create Compute*

Bottom-right: Create Compute. Click it.

*Wait for Cluster Startup*

Status will change: Pending -> Starting -> Running

Wait until you see: 🟢 Running

This usually takes 2–5 minutes.

**Option B**: Attach Existing Cluster*

If you already have a cluster running: Open Notebook
Open:
- 01_enhanced_data_model.py (this one) or 01_enhanced_data_model notebook

*Top Right Corner*

You will see: Connect or Detached. Click it.

*Select Cluster*

Choose: **upi-cdc-cluster** (or your existing cluster). Click: Attach

Wait a few seconds.

You should now see: Connected to **upi-cdc-cluster**

**Run the data model file first**

Go to Workspace

Open **UPI_Transactions_CDC_Project**

Open: **01_enhanced_data_model.py**

At the top right, attach the cluster **upi-cdc-cluster**

Click: Run all

This creates:
- gds_de_bootcamp_new.default.**raw_upi_transactions_v1**
- gds_de_bootcamp_new.default.**merchant_aggregations**

**Start the streaming pipeline**

Open: 
- **02_realtime_streaming_pipeline.py**

Attach the same cluster

Click: Run all

This starts the real-time streaming job. It reads from the CDC feed on **raw_upi_transactions_v1** and updates **merchant_aggregations.**

**Generate mock CDC data**

Open:
- **03_enhanced_mock_data_generator.py**

Attach the same cluster

Click: Run all

This inserts initial transactions and then continuously performs INSERT, UPDATE, and DELETE operations for CDC testing.

**Optional CDC test**

Use this only if you want to see CDC changes printed directly.

Open:
- **test.py**
 
Attach the cluster

Click: Run all

Important: this file reads from raw_upi_transactions, but your main table is **raw_upi_transactions_v1**, so update the table name before running.

Change:

<img width="415" height="66" alt="image" src="https://github.com/user-attachments/assets/05a08d0e-1e63-441c-a5f0-0becbd46f099" />

to:

<img width="416" height="68" alt="image" src="https://github.com/user-attachments/assets/93aa4d8b-f153-46b9-8b11-c1684e438672" />


<img width="506" height="463" alt="image" src="https://github.com/user-attachments/assets/6d8e37bc-6f0c-4c45-9f3e-6f95a9a63d55" />

**Execution order**

Run the files in this order:
- 01_enhanced_data_model.py
- 02_realtime_streaming_pipeline.py
- 03_enhanced_mock_data_generator.py
- test.py (optional)

**End-to-end architecture**

<img width="516" height="309" alt="image" src="https://github.com/user-attachments/assets/5efc7277-d5d6-450f-a20c-df9ffc452a76" />





