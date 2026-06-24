I have this project FlyHigh Airways Real-Time Flight Booking Data Ingestion Pipeline Project.

<img width="679" height="342" alt="image" src="https://github.com/user-attachments/assets/ff6c861b-083a-4b3b-a10b-fac25e573544" />

<img width="733" height="152" alt="image" src="https://github.com/user-attachments/assets/bd551a65-645b-4e17-ad87-77c0d8b73210" />

<img width="743" height="212" alt="image" src="https://github.com/user-attachments/assets/ae75b481-9e9b-4337-a602-6177cd49c3fd" />

<img width="722" height="154" alt="image" src="https://github.com/user-attachments/assets/307761a5-951e-4d04-a1e5-9ea59c4398b4" />

Project Name: **Flight Booking Real-Time Data Ingestion Pipeline on AWS**

This project ingests flight bookings, cancellations, and search queries in real time, processes them with AWS services, stores historical data, updates flight capacity, and sends high-demand alerts.

<img width="640" height="449" alt="image" src="https://github.com/user-attachments/assets/0e9b17dc-cc1a-4688-a7f1-e4d76660d44f" />

**End-to-End Architecture**

<img width="544" height="279" alt="image" src="https://github.com/user-attachments/assets/8fda3c85-95bc-42fc-9f36-87508d3e5e31" />

The uploaded solution describes **API Gateway, Lambda, Kinesis Data Streams, Kinesis Data Analytics, DynamoDB, S3, Redshift, CloudWatch, SNS, and QuickSight as the main AWS components.**

**Step-by-Step Execution in AWS GUI**

**1. Create S3 Bucket**

Go to AWS Console ➜ S3 ➜ Create bucket.

Create a bucket like: **flight-booking-realtime-pipeline**

Inside the bucket, create folders:
- raw/
- processed/
- redshift/
- logs/

Upload documentation files here if needed:
- README.md
- architecture.md
- AWS_Design_Assignment_1.pdf
- AWS_Design_Assignment_Solution_1.pdf

**2. Create Kinesis Data Stream**

Go to AWS Console ➜ Kinesis ➜ Data Streams ➜ Create data stream.

Use:
- Stream name: **flight-booking-stream**
- Capacity mode: On-demand

This stream receives booking, cancellation, and search events in real time.

**3. Create DynamoDB Tables**

Go to DynamoDB ➜ Tables ➜ Create table.

Create table 1:
- Table name: **flight_capacity**
- Partition key: flight_id

Create table 2:
- Table name: **booking_events**
- Partition key: booking_id

DynamoDB stores current flight inventory and booking/cancellation status.

**4. Create Lambda Functions**

Go to Lambda ➜ Create function ➜ Author from scratch.

Create these Lambda functions:
- **api_booking_handler**
- **high_demand_alert**
- **kinesis_to_s3**
- **update_capacity**

For each function:
- Choose Python 3.11 or Python 3.12
- Open Code
- Delete the default code
- Paste the matching .py file
- Click Deploy

Lets explain this in detail.

**Exact GUI Steps — Create the Lambda Functions**

You need to create 4 separate Lambda functions:
- **api_booking_handler**
- **high_demand_alert**
- **kinesis_to_s3**
- **update_capacity**

**Function 1: api_booking_handler**

*Step 1*

Login to AWS Console.

Search: Lambda. Click: Lambda

*Step 2*

Click the orange button: Create function

*Step 3*

Select: Author from scratch

*Step 4*

Fill in:
- Function name: **api_booking_handler**
- Runtime: Select: Python 3.12 (or Python 3.11)
- Architecture: x86_64

Leave everything else as default.

*Step 5*

Click: Create function

Wait until Lambda opens.

*Step 6*

Scroll down to: Code source

You will see:

<img width="315" height="150" alt="image" src="https://github.com/user-attachments/assets/f9337344-c805-4d3d-a1ac-8a7c5e492688" />

In our script looks like:

<img width="465" height="158" alt="image" src="https://github.com/user-attachments/assets/76601be7-1ea6-4660-b5a5-b91b5fea7855" />

*Step 7*

Delete everything.

Paste:

<img width="288" height="129" alt="image" src="https://github.com/user-attachments/assets/af4d2945-38fd-4e32-b22c-3971e23414f2" />

*Step 8*

Click the orange button: Deploy. Top right.

Wait for: Successfully updated function

**Function 2: high_demand_alert**

Return to: Lambda Console
- Click: Create function
- Select: Author from scratch

Fill:
- Function Name
- high_demand_alert
- Runtime
- Python 3.12

Click: Create function

Delete default code.

Paste:

<img width="299" height="72" alt="image" src="https://github.com/user-attachments/assets/d838c939-649c-4de7-9f8c-3a29d4fff3b4" />

In our code looks like:

<img width="424" height="134" alt="image" src="https://github.com/user-attachments/assets/06727ed3-e716-4856-b751-4650dd3f1508" />

Click: Deploy

**Function 3: kinesis_to_s3**

Click: Lambda → Create function
- Select: Author from scratch
- Function Name: kinesis_to_s3
- Runtime: Python 3.12

Click: Create function

Delete default code.

Paste:

<img width="275" height="78" alt="image" src="https://github.com/user-attachments/assets/2ae61868-d9c1-47d7-8eba-f0e82d1d1191" />

In our code looks like:

<img width="376" height="131" alt="image" src="https://github.com/user-attachments/assets/fcff6718-25f2-48ee-8731-6baeb859db85" />

Click: Deploy

**Function 4: update_capacity**

Click: Create function
-Select: Author from scratch
-Function Name: update_capacity
-Runtime: Python 3.12

Click: Create function

Delete default code.

Paste:

<img width="286" height="75" alt="image" src="https://github.com/user-attachments/assets/6e08243a-1b12-4525-8b86-2df0e508bba4" />

In our code looks like:

<img width="404" height="142" alt="image" src="https://github.com/user-attachments/assets/8c695e05-7bca-4c2e-b722-d9a06f35cf0b" />

Click: Deploy

**Verify All Functions Exist**

Go to:
- AWS Console
  - → Lambda
  - → Functions

You should see:
- **api_booking_handler**
- **high_demand_alert**
- **kinesis_to_s3**
- **update_capacity**

Lets continue.

**5. Connect API Gateway to Lambda**

Go to API Gateway → Create API → HTTP API.

Create routes:
- POST /booking
- POST /cancel
- POST /search

Integration:
- Lambda: **api_booking_handler**

Click:
- Deploy → Create stage → prod

Your users will send booking requests to the API Gateway URL.

Lets explain this in detail.

**Exact GUI Steps — Connect API Gateway to Lambda**

*Step 1 — Open API Gateway*

Login to AWS Console.

In the search bar type: API Gateway
- Click: Amazon API Gateway

*Step 2 — Create API*

Click: Create API

You will see several options:
- HTTP API
- REST API
- WebSocket API

Under HTTP API, click:
- Build

*Step 3 — Add Integration*

You will be on:

Choose an integration
- Select: Lambda

*Step 4 — Select Lambda Function*

In the Lambda search box: **api_booking_handler**

Select: **api_booking_handler**

Click: Next

*Step 5 — Configure Routes*

You should now be on:

Configure routes. Click: Add route

Create Route #1
- Method: POST
- Resource Path: /booking

Click: Add

Create Route #2

Click: Add route

- Method: POST
- Resource Path: /cancel

Click: Add

Create Route #3

Click: Add route

- Method: POST
- Resource Path: /search

Click:Add

You should now see:
- POST /booking
- POST /cancel
- POST /search

*Step 6 — Attach Lambda to Routes*

For each route:
- POST /booking
- POST /cancel
- POST /search

Select: **api_booking_handler**

as the integration target.

Click: Next

*Step 7 — Configure Stage*

Stage Name: prod

Leave defaults.

Click: Next

*Step 8 — Review*

You should see something similar to: API Type: HTTP API

Routes:
- POST /booking
- POST /cancel
- POST /search

Integration: api_booking_handler

Stage: prod

Click: Create

*Step 9 — Copy API Endpoint*

After creation AWS shows: Invoke URL
- Example: https://abc123xyz.execute-api.us-east-1.amazonaws.com

Copy this URL.

*Step 10 — Verify Routes*

In API Gateway:

- Your API
  - → Routes

You should see:
- POST /booking
- POST /cancel
- POST /search

*Step 11 — Test the API*

Open:
- API Gateway
  - → Your API
  - → Routes
  - → POST /booking

Click: Test

Request Body:

<img width="279" height="115" alt="image" src="https://github.com/user-attachments/assets/4f07be9c-76d3-4454-aaa8-8e382697cc68" />

Click: Send

Expected Lambda response:

<img width="254" height="102" alt="image" src="https://github.com/user-attachments/assets/c2c02496-641b-4a5b-a80c-19989c48b534" />

*Step 12 — Test Using Browser/Postman*

Use: https://YOUR_API_ID.execute-api.REGION.amazonaws.com/prod/booking

Example: https://abc123xyz.execute-api.us-east-1.amazonaws.com/prod/booking

Send: POST

with:

<img width="266" height="85" alt="image" src="https://github.com/user-attachments/assets/3cdbcccb-5924-41f1-a46c-128678953ffc" />

Lambda will process the request and later send booking events into Kinesis.

**6. Connect Lambda to Kinesis**

Open Lambda: **api_booking_handler**

Go to: Configuration → Permissions → Execution role

Add permission for:
- kinesis:PutRecord
- kinesis:PutRecords

Target stream: **flight-booking-stream**

Lets explain this in detail.

**Exact GUI Steps — Connect Lambda to Kinesis**

At this point you should already have:
- ✅ Lambda Function: **api_booking_handler** 
- ✅ Kinesis Data Stream: **flight-booking-stream**

If you have not created the Kinesis stream yet:
- AWS Console
  - → Kinesis
  - → Data Streams
  - → Create data stream

Name: **flight-booking-stream**

Capacity Mode: On-demand

Click: Create data stream

Wait until the status becomes: Active

*Step 1 — Open Lambda*

Go to:
- AWS Console
  - → Lambda
  - → Functions

Click: **api_booking_handler**

*Step 2 — Open Configuration*

Inside the Lambda function click: Configuration. Tab located near:
- Code
- Test
- Monitor
- **Configuration**
- Aliases
- Versions

*Step 3 — Open Permissions*

Inside Configuration click: Permissions

Scroll down until you see: Execution role
- Example: **api_booking_handler-role-xxxxxxxx**

*Step 4 — Open IAM Role*

Click the role name. 
- Example: **api_booking_handler-role-xxxxxxxx**

AWS opens IAM in a new tab.

*Step 5 — Add Permissions*

Click: Add permissions

Choose: Attach policies

*Step 6 — Attach Kinesis Policy*

Search: AmazonKinesisFullAccess. Check the box.

Click: Add permissions

*Step 7 — Attach DynamoDB Policy*

Again click: Add permissions
- → Attach policies. Search: AmazonDynamoDBFullAccess. Check the box.

Click: Add permissions

*Step 8 — Verify Policies*

You should now see:
- AmazonKinesisFullAccess
- AmazonDynamoDBFullAccess

under: Permissions policies

*Step 9 — Return to Lambda*

Go back to: Lambda → **api_booking_handler**

*Step 10 — Modify Lambda Code*

Open: Code

Replace the simple code with:

<img width="334" height="317" alt="image" src="https://github.com/user-attachments/assets/ccea86d2-55df-4789-895a-c4bbd3882713" />

*Step 11 — Deploy*

Click: Deploy

Top-right corner.

Wait for: Successfully updated function

*Step 12 — Create Test Event*

Click: Test

Near Deploy button.

*Step 13 — Configure Test Event*

Event Name: **booking_test**

Template: **Hello World**

Replace JSON with:

<img width="312" height="128" alt="image" src="https://github.com/user-attachments/assets/c6dbb605-1b93-43c4-84f9-e222ee781442" />

Click: Save

*Step 14 — Run Test*

Click: Test

Again.

Expected result:

<img width="255" height="100" alt="image" src="https://github.com/user-attachments/assets/217ada47-462f-45b5-a485-ef67568452fc" />

*Step 15 — Verify Record Reached Kinesis*

Go to:
- AWS Console
  - → Kinesis
  - → Data Streams

Click: **flight-booking-stream**

Open: Monitoring

You should see metrics increasing:
- Incoming Records
- Incoming Bytes
- Put Records Success

This confirms Lambda successfully wrote data into Kinesis.

Lets continue.

**7. Connect Kinesis to Processing Lambdas**

Go to Lambda → **kinesis_to_s3** → Add trigger.

Choose:
- Trigger: Kinesis
- Stream: **flight-booking-stream**
- Batch size: 100

Repeat for:
- **high_demand_alert**
- **update_capacity**

Lets explain this in detail.

**Exact GUI Steps — Connect Kinesis to Processing Lambdas**

At this stage you should already have: **flight-booking-stream**

and these Lambda functions:
- **kinesis_to_s3**
- **high_demand_alert**
- **update_capacity**

*Part 1 — Connect Kinesis to **kinesis_to_s3***

*Step 1*

Go to:
- AWS Console
  - → Lambda
  - → Functions

Click: **kinesis_to_s3**

*Step 2*

Inside the function page click: Add trigger

You can find it near the top-left of the Designer section.

*Step 3*

Under Trigger Configuration:

Select: Kinesis

*Step 4*

Configure Trigger

Kinesis Stream. Choose:
- **flight-booking-stream**

Batch Size
- Enter: 100

Starting Position
- Select: Latest

This means Lambda only processes new records arriving after the trigger is attached.

Batch Window
- Leave: 0 (Default)

Retry Attempts
- Leave default.

Enable Trigger
- Check: Enable trigger

*Step 5*

Click: Add

Wait a few seconds.

You should now see:

Kinesis
│
▼
flight-booking-stream
│
▼
kinesis_to_s3

*Part 2 — Connect Kinesis to **high_demand_alert***

*Step 1*

Return to: Lambda. → Functions
- Click: **high_demand_alert**

*Step 2*

Click: Add trigger

*Step 3*

Choose: Kinesis

*Step 4*

Configure. Stream
- **flight-booking-stream**

- Batch Size: 100
- Starting Position: Latest

Enable Trigger: Checked

*Step 5*

Click: Add

You should now have:

flight-booking-stream
        │
        ▼
high_demand_alert

*Part 3 — Connect Kinesis to **update_capacity***

*Step 1*

Go to:
- Lambda
  - → Functions

Click: **update_capacity**

*Step 2*

Click: Add trigger

*Step 3*

Select: Kinesis

*Step 4*

Configure. Stream
- **flight-booking-stream**

- Batch Size: 100
- Starting Position: Latest
- Enable Trigger: Checked

*Step 5*

Click: Add

*Verify All Triggers*

Go to:
- Lambda
  - → Functions

Open each Lambda:
- **kinesis_to_s3**
- **high_demand_alert**
- **update_capacity**

Under Configuration → Triggers you should see:
- **flight-booking-stream**

attached to all three.

Lets continue.

**8. Create SNS Alert**

Go to SNS → Topics → Create topic.

Use:
- Topic name: **high-demand-route-alerts**
- Type: Standard

Create subscription:
- Protocol: Email
- Endpoint: your email

Confirm the email subscription from your inbox.

Use this topic for high-demand route notifications.

**9. Create Redshift Cluster or Serverless**

Go to Amazon Redshift → Serverless → Create workgroup and namespace.

Then open: Query Editor v2

Run:
- -- bookings, searches, cancellations tables

Use your **redshift_tables.sql** file here.

<img width="416" height="93" alt="image" src="https://github.com/user-attachments/assets/4d05eb9b-3f29-4bd9-9a27-54e094653eaf" />

Redshift stores historical booking/search/cancellation data for analytics.

**10. Load S3 Data into Redshift**

In Redshift Query Editor v2, use a COPY command like:

<img width="279" height="98" alt="image" src="https://github.com/user-attachments/assets/9a3d0f41-9bf0-4190-96f6-b0cd55388808" />

This loads historical S3 data into Redshift.

**11. Create QuickSight Dashboard**

Go to Amazon QuickSight → Datasets → New dataset.

Choose: Redshift. Connect to your Redshift database.

Create visuals for:
- Bookings by route
- Cancellations by route
- High-demand routes
- Search trends
- Available capacity

QuickSight is used by analysts to view the Redshift analytics dashboard.

**12. Add CloudWatch Monitoring**

Go to CloudWatch → Alarms → Create alarm.

Create alarms for:
- Kinesis incoming records
- Lambda errors
- Lambda duration
- Kinesis iterator age
- DynamoDB throttles

The assignment expects scalability, monitoring, fault tolerance, and low-latency processing.


**Final Workflow**

- 1 User books, cancels, or searches a flight.
- 2 API Gateway receives the request.
- 3 Lambda processes the request.
- 4 Lambda sends event data to Kinesis.
- 5 Kinesis streams the data in real time.
- 6 Lambda updates DynamoDB capacity.
- 7 Kinesis Analytics detects high-demand routes.
- 8 SNS sends alerts.
- 9 Lambda archives data to S3.
- 10 Redshift loads S3 data for historical analytics.
- 11 QuickSight displays dashboards.
- 12 CloudWatch monitors the full pipeline.









