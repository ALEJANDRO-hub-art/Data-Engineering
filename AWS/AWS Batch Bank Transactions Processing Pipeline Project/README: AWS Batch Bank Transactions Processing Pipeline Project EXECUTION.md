I have this project AWS Batch Bank Transactions Processing Pipeline Project.

<img width="726" height="271" alt="image" src="https://github.com/user-attachments/assets/c4075447-156f-48fe-822f-afe49502df6e" />

<img width="733" height="157" alt="image" src="https://github.com/user-attachments/assets/7e11bb67-875b-4567-ad69-24ebfa5a0964" />

<img width="731" height="172" alt="image" src="https://github.com/user-attachments/assets/fe559132-8082-476e-8891-99c309230139" />

<img width="764" height="151" alt="image" src="https://github.com/user-attachments/assets/95bc2324-cab3-4bb5-a066-7c5e7c081bd2" />

<img width="745" height="154" alt="image" src="https://github.com/user-attachments/assets/7c485bba-9787-4216-bd53-a244b560119f" />

<img width="751" height="146" alt="image" src="https://github.com/user-attachments/assets/189a6e72-a3db-4d3a-a296-6ce05e014dba" />

This is one complete AWS data engineering project, not mini projects.

What the project does

A daily bank transactions JSON file is uploaded to Amazon S3. That upload automatically triggers AWS Lambda, which starts an AWS Glue ETL job. Glue cleans the data, removes bad/null records, removes duplicate transaction_id records, converts the data to Parquet, saves it back to S3, and makes it queryable in Amazon Athena. The project also uses CloudWatch + SNS for monitoring and alerts.

Files and where to upload them

<img width="658" height="489" alt="image" src="https://github.com/user-attachments/assets/7f23f7ef-fa0e-4f53-a2f8-6aaecc810925" />

**S3 folder structure**

Create one S3 bucket, for example:

<img width="257" height="137" alt="image" src="https://github.com/user-attachments/assets/0866c309-1ad9-4adf-8d4a-94322a8af934" />

**End-to-end architecture**

<img width="437" height="459" alt="image" src="https://github.com/user-attachments/assets/55cf48d4-b31c-4776-bb85-7ea03b38c8e3" />

**Step-by-step execution in AWS GUI**

**Step 1 — Create the S3 bucket**

Open AWS Console. Search S3. Click Create bucket.
- Bucket name: **bank-transactions-pipeline-yourname.**
- Region: choose your region.

Leave default settings. Click Create bucket.

Open the bucket. Click Create folder.

Create these folders:
- raw
- processed
- scripts
- athena-results

**Step 2 — Upload files to S3**

Open your S3 bucket. Open the **raw/** folder. Click Upload.

Upload:
- **transactions_sample.json**
- **transactions_2026-04-16.json**
 
Go back to bucket root. Open **scripts/.**
- Upload: **glue_bank_transactions_etl.py**

**Step 3 — Create SNS topic**

Search SNS. Click Topics. Click Create topic.
- Type: Standard.
- Name: bank-transaction-alerts

Click Create topic.

Click Create subscription.

- Protocol: Email.
- Endpoint: your email.

Click Create subscription.

Open your email and confirm the subscription.

**Step 4 — Create IAM role for Lambda**

Search IAM. Click Roles. Click Create role.
- Trusted entity: AWS service.
- Use case: Lambda.

Click Next.

Add permissions:
- AWSLambdaBasicExecutionRole
- AmazonS3ReadOnlyAccess
- AWSGlueServiceRole
- AmazonSNSFullAccess

Role name: **lambda-glue-trigger-role**

Click Create role.

Lets explain this in detail.

**Exact GUI Steps — Create IAM Role for Lambda**

*Step 1 — Open IAM*

Sign in to the AWS Console.

In the search bar at the top, type: IAM. Click IAM.

*Step 2 — Open Roles*

In the left navigation pane:

<img width="151" height="49" alt="image" src="https://github.com/user-attachments/assets/3cd5772e-4343-4e26-a885-d7aa16d90dd3" />

Click Roles.

*Step 3 — Create Role*

Click the orange Create role button in the upper-right corner.

*Step 4 — Select Trusted Entity*

Under Trusted entity type: Select: AWS service

Under Use case: Select: Lambda

Your screen should look similar to:
- Trusted entity type
  - ◉ AWS service
- Use case
  - ◉ Lambda

Click: Next

*Step 5 — Add Permissions*

You will now be on: Add permissions

In the search box, search and select the following policies one by one.

- Policy 1. Search: **AWSLambdaBasicExecutionRole**. Check the box.
- Policy 2. Search: **AmazonS3ReadOnlyAccess**. Check the box.
- Policy 3. Search: **AWSGlueServiceRole**. Check the box.
- Policy 4. Search: **AmazonSNSFullAccess**. Check the box.

You should now have four checked policies:
- ✓ AWSLambdaBasicExecutionRole
- ✓ AmazonS3ReadOnlyAccess
- ✓ AWSGlueServiceRole
- ✓ AmazonSNSFullAccess

Click: Next

*Step 6 — Name the Role*

Role name: **lambda-glue-trigger-role**

Description (optional): Allows Lambda to start Glue jobs, read S3 files, write CloudWatch logs, and send SNS notifications.

Click: Create role

*Step 7 — Verify Role Creation*

You should now see:

<img width="202" height="49" alt="image" src="https://github.com/user-attachments/assets/f34220ab-57ae-4466-8254-bc158b20a832" />

Click the role name.

You should see: Permissions policies
- AWSLambdaBasicExecutionRole
- AmazonS3ReadOnlyAccess
- AWSGlueServiceRole
- AmazonSNSFullAccess

**Step 5 — Create Lambda trigger function**

Search Lambda. Click Create function. Choose Author from scratch.
- Function name: **lambda-trigger-glue**
- Runtime: Python 3.11.
- Execution role: choose lambda-glue-trigger-role.

Click Create function.

Open the code editor.

Paste the code from: **lambda_trigger_glue.py**

Click Deploy.

Go to Configuration → Environment variables.

Add:
- GLUE_JOB_NAME = **bank-transactions-etl-job**
- SNS_TOPIC_ARN = **your SNS topic ARN**

Lets explain this in detail.

**Create Lambda Trigger Function (Exact AWS GUI Steps)**

*1. Open AWS Lambda*

Sign in to AWS Console. In the top search bar type: Lambda

Click Lambda.

You should arrive at:

<img width="206" height="92" alt="image" src="https://github.com/user-attachments/assets/6847247b-5353-4d51-8ee5-632aae474d43" />

*2. Create Function*
  
Click the orange Create function button.

You will see three options:
- ◉ Author from scratch
- ○ Use a blueprint
- ○ Container image

Select: Author from scratch

*3. Configure Function*

Function name
- Enter: **lambda-trigger-glue**

Runtime. Open the dropdown.
- Select: Python 3.11 (If 3.11 isn't available, choose the latest Python version.)

Architecture. 
- Leave: x86_64

*4. Configure Execution Role*

Scroll down to: Change default execution role. Click the dropdown arrow.
- Select: Use an existing role

A new field appears.

- Choose: **lambda-glue-trigger-role** (the IAM role you created in Step 4)

Your screen should look like:

Execution role
- ○ Create a new role with basic Lambda permissions
- ◉ Use an existing role

Existing role: **lambda-glue-trigger-role**

*5. Create Function*

Click: Create function

AWS will create the Lambda. Wait about 10–20 seconds.

You will be redirected to:

<img width="165" height="49" alt="image" src="https://github.com/user-attachments/assets/c5781a40-84b8-4a0e-820b-16073c05d8f2" />

*6. Open Code Editor*

Scroll down. You will see:
- Code source

with a file similar to:
- **lambda_function.py**

Delete all existing code.

*7. Paste lambda_trigger_glue.py Code*

Open your local file: **lambda_trigger_glue.py**. Copy everything. Paste it into the Lambda editor.

The code starts with:

<img width="248" height="89" alt="image" src="https://github.com/user-attachments/assets/92050601-6f7a-4671-9a05-fcb593d85d18" />

and contains:

<img width="221" height="51" alt="image" src="https://github.com/user-attachments/assets/f85ac9ea-ddc5-4d4e-890f-27380c3a1ca8" />

which starts the Glue ETL job.

*8. Deploy the Function*

At the top of the editor click: Deploy

Wait for: Successfully updated function

to appear.

*9. Configure Environment Variables*

Near the top click: Configuration

Then click: Environment variables

Then click: Edit

Then: Add environment variable

*Variable #1*
- Key: **GLUE_JOB_NAME**
- Value: **bank-transactions-etl-job**

*Variable #2*
- Key: **SNS_TOPIC_ARN**
- Value: **Paste the ARN of your SNS topic. Example: arn:aws:sns:us-east-1:123456789012:bank-transaction-alerts**

*Where do I find the SNS ARN?*

Open AWS Console. Search: SNS
- Click Topics.
- Click: **bank-transaction-alerts**
- Copy the value shown under: Topic ARN
  - Example: arn:aws:sns:us-east-1:123456789012:bank-transaction-alerts
  
Paste it into the Lambda environment variable.

*10. Save Environment Variables*

Click: Save

You should now see:

<img width="452" height="102" alt="image" src="https://github.com/user-attachments/assets/db291c69-5535-484b-814a-5db96bc03214" />

*Verify Lambda Configuration*

Click: Configuration

Then: General configuration

Verify:
- Function Name: **lambda-trigger-glue**
- Runtime: Python 3.11
- Execution Role: **lambda-glue-trigger-role**

**Step 6 — Add S3 trigger to Lambda**

In the Lambda function, click Add trigger.

Source: S3.

Bucket: your bucket.

Event type: All object create events.

Prefix: raw/

Suffix: .json

Click Add.

Lets explain this in detail.

**Add S3 Trigger to Lambda (Exact AWS GUI Steps)**

This step connects your S3 bucket to Lambda so that every time a JSON file is uploaded into the **raw/** folder, Lambda automatically starts the Glue job.

*1. Open Lambda*

Log in to AWS Console. Search: Lambda


Click Lambda.

Click your function: **lambda-trigger-glue**

*2. Open Function Overview*

You will see something similar to:

<img width="140" height="142" alt="image" src="https://github.com/user-attachments/assets/77c306b6-3c9c-4e39-854e-a02d8d4d99cc" />

On the left side of the diagram click: + Add trigger

*3. Select Trigger Source*

A panel opens on the left. Under: Select a source. Choose: S3

*4. Configure S3 Trigger*

Bucket
- Under:Bucket

Select your bucket. Example: **bank-transactions-pipeline-alejandro**

Event Type
- Under: Event type

Open dropdown. Select: All object create events

This means Lambda will run whenever a new file is uploaded.

*5. Configure Prefix Filter*

Expand: Additional settings

Check: Prefix

Enter: **raw/**

This tells Lambda: Only monitor files uploaded into: **raw/**

Examples that WILL trigger:
- **raw/transactions_2026-04-16.json**
- **raw/transactions_sample.json**

Examples that will NOT trigger:
- **processed/file.parquet**
- **scripts/glue_bank_transactions_etl.py**
- **athena-results/output.csv**

*6. Configure Suffix Filter*

Check: Suffix

Enter: .json

This tells Lambda: Only trigger on JSON files

Examples that WILL trigger:
- **transactions_2026-04-16.json**
- **transactions_sample.json**

Examples that will NOT trigger:
- **transactions.csv**
- **transactions.parquet**
- **transactions.txt**

*7. Acknowledge Recursive Trigger Warning*

Near the bottom you'll see: Recursive invocation

Check: I acknowledge that using the same S3 bucket for input and output could cause recursive invocations.

This warning appears because the bucket contains both:
- raw/
- processed/

However your Lambda code only processes:

<img width="382" height="69" alt="image" src="https://github.com/user-attachments/assets/3480cedd-c33c-4bbd-9f51-0e3b6fd96858" />

so processed files will be ignored.

*8. Add Trigger*

Click: Add

AWS creates the connection.

*9. Verify Trigger*

Back in Function Overview you should now see:

<img width="151" height="92" alt="image" src="https://github.com/user-attachments/assets/42c962c8-076e-46b8-8c29-b17595664b36" />

or

<img width="237" height="164" alt="image" src="https://github.com/user-attachments/assets/41300fa4-5f0a-4d32-bbba-13d0fd071929" />

*10. Test the Trigger*

Open S3. Search: S3

Open your bucket. Open: **raw/**
- Click: Upload. Upload: **transactions_sample.json** or **transactions_2026-04-16.json**

*11. Verify Lambda Ran*

Return to:
- Lambda
  - → lambda-trigger-glue

Click: Monitor

Then: View CloudWatch Logs

You should see a recent invocation.

<img width="545" height="540" alt="image" src="https://github.com/user-attachments/assets/02ffe3d0-63c5-49b9-9ab1-dd95078faff2" />

**Step 7 — Create Glue job**

Search AWS Glue. Click ETL jobs. Click Create job.

Choose Script editor
.
Choose Upload and edit existing script or paste script manually.

Use script: **glue_bank_transactions_etl.py**

- Job name: **bank-transactions-etl-job**
- IAM role: choose or create a Glue role with S3 access.
- Language: Python.
- Type: Spark.

Save the job.

**Step 8 — Test the pipeline**

Go to S3. Open **raw/.**. 
- Upload: **transactions_sample.json**
 
This should trigger Lambda. Lambda starts Glue.

Glue writes cleaned Parquet files to:
- s3://your-bucket/processed/

**Step 9 — Check CloudWatch logs**

Search CloudWatch. Click Log groups.

Open Lambda log group: **/aws/lambda/lambda-trigger-glue**

Check if Glue job started successfully.

Also check Glue job logs for source count, processed count, and rejected count.

**Step 10 — Create Glue crawler for Athena**

Open AWS Glue. Click Crawlers. Click Create crawler.

Name: **bank-transactions-processed-crawler**

Data source: S3. 

S3 path: **s3://your-bucket/processed/**

Create database: **bank_transactions_db**

Run crawler.

**Step 11 — Query in Athena**

Search Athena. Open Query editor.
- Set query result location: **s3://your-bucket/athena-results/**
- Select database: **bank_transactions_db**

Run:

<img width="189" height="84" alt="image" src="https://github.com/user-attachments/assets/e281f7bb-3804-4af8-936d-2e2163ccc3e9" />

**Final workflow summary**

You generate or upload a daily JSON file
- → File lands in S3 raw/
- → S3 triggers Lambda
- → Lambda starts Glue job
- → Glue cleans and deduplicates data
- → Glue writes Parquet to S3 processed/
- → Glue Crawler creates Athena table
- → Athena queries clean bank transactions
- → CloudWatch monitors logs
- → SNS sends failure or missing-file alerts





