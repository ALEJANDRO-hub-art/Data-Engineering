I have this project AWS Event-Driven Data Processing & Messaging Projects.

<img width="589" height="104" alt="image" src="https://github.com/user-attachments/assets/3f1dd8d8-34f8-4b77-8c62-1f3549156ee5" />

This is not one single project. **It is a collection of 5 AWS Event-Driven Architecture mini-projects**, each demonstrating a different AWS integration pattern.

 <img width="284" height="159" alt="image" src="https://github.com/user-attachments/assets/91a7ef9f-98a8-4814-8959-242120588a7e" />

**Mini Project 1: EventBridge Pipes**

Folder: 2 Event_Bridge_Pipe

Purpose:
- Demonstrates:

Producer
<br>⬇️
<br>SQS Queue
<br>⬇️
<br>EventBridge Pipe
<br>⬇️
<br>Filtering
<br>⬇️
<br>Transformation
<br>⬇️
<br>Target Service

The sample file contains:
- Purchase order messages
- Event filtering
- Event transformation

Architecture:

Application 
<br>⬇️
<br>SQS
<br>⬇️
<br>EventBridge Pipe
<br>⬇️
<br>Filter Events
<br>⬇️
<br>Transform Payload
<br>⬇️
<br>Target Service

**Mini Project 2: S3 Data**

Folder: 3 S3_Data

Purpose:
- Contains sample CSV data: **store_data.csv**

Used as source data for S3 processing demonstrations.

Workflow:

CSV File
<br>⬇️
<br>S3 Bucket
<br>⬇️
<br>Consumed by Lambda

**Mini Project 3: S3 → Lambda**

Folder: 4 S3_To_Lambda

Purpose: Shows how a Lambda is automatically triggered when a file is uploaded to S3.

The Lambda:
- Receives S3 event
- Reads bucket name
- Reads uploaded file
- Loads CSV into pandas
- Processes data

Architecture:

CSV File
<br>⬇️
<br>S3 Bucket
<br>⬇️
<br>S3 Event Notification
<br>⬇️
<br>Lambda
<br>⬇️
<br>Pandas Processing

**Mini Project 4: SNS Notifications**

Folder: 5 SNS

Purpose:
- Extends the S3 → Lambda pattern.

The Lambda:
- Reads S3 file
- Processes CSV
- Sends SUCCESS notification to SNS
- Sends FAILURE notification if processing fails

Architecture:

CSV File
<br>⬇️
<br>S3 Bucket
<br>⬇️
<br>Lambda
<br>⬇️
<br>SNS Topic
<br>⬇️
<br>Email / Subscribers

**Mini Project 5: SQS Messaging**

Folder: 6 SQS

Contains three Lambda functions: **mock generator lamba.py, auto consumer from sqs lamba.py, manual consumer from sqs lambda.py**

*Producer Lambda*

**mock generator lamba.py**
- Generates sales orders and pushes them into SQS.

Lambda Producer
<br>⬇️
<br>SQS Queue

*Automatic Consumer*

**auto consumer from sqs lamba.py**
- Lambda triggered automatically by SQS. Processes batches of messages.

SQS
<br>⬇️
<br>Lambda Trigger
<br>⬇️
<br>Process Messages

*Manual Consumer*

**manual consumer from sqs lambda.py**
- Lambda polls SQS manually. Reads messages and deletes them after processing.

Lambda
<br>⬇️
<br>Poll SQS
<br>⬇️
<br>Process Messages
<br>⬇️
<br>Delete Messages

**Big Picture**

All folders together form an: AWS Event-Driven Serverless Architecture Learning Portfolio

End-to-End Services Covered:

S3
<br>⬇️
<br>Lambda
<br>⬇️
<br>SNS

SQS
<br>⬇️
<br>Lambda

SQS
<br>⬇️
<br>EventBridge Pipes
<br>⬇️
<br>Filtering
<br>⬇️
<br>Transformation
<br>⬇️
<br>Target

-------------------------------------------------------------------------------------------------------------------------------------

Lets get into the EXECUTION of the project.

This is one project with mini modules:
- S3 → Lambda → SNS
- Lambda → SQS → Lambda Consumer
- SQS → EventBridge Pipe → Filter/Transform → Target

Files and where to upload them

<img width="667" height="451" alt="image" src="https://github.com/user-attachments/assets/f648e941-1b2c-4757-8fe2-2e0b25c19ce2" />


- S3 → Lambda → SNS
CSV File
<br>⬇️
<br>Amazon S3 Bucket
<br>⬇️
<br>S3 Event Trigger
<br>⬇️
<br>AWS Lambda
<br>⬇️
<br>Read CSV with pandas
<br>⬇️
<br>CloudWatch Logs
<br>⬇️
<br>SNS Notification

- Lambda → SQS → Lambda Consumer
Mock Generator Lambda
<br>⬇️
<br>Amazon SQS Queue
<br>⬇️
<br>Lambda Consumer
<br>⬇️
<br>Process Messages
<br>⬇️
<br>CloudWatch Logs

- SQS → EventBridge Pipe → Filter/Transform → Target
SQS Queue
<br>⬇️
<br>EventBridge Pipe
<br>⬇️
<br>Filter Events
<br>⬇️
<br>Transform Payload
<br>⬇️
<br>Target Service








