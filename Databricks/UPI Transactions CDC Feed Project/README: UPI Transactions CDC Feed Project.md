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

*Upload the Python files*
Open the folder **UPI_Transactions_CDC_Project**
- Click Create
- Click File

Upload these files one by one:
- 01_enhanced_data_model(2).py
- 02_realtime_streaming_pipeline(2).py
- 03_enhanced_mock_data_generator(2).py
- test.py
- README.md















