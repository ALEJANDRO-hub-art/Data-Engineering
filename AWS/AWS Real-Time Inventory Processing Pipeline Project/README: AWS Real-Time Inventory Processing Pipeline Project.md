I have this project AWS Real-Time Inventory Processing Pipeline Project.

<img width="669" height="253" alt="image" src="https://github.com/user-attachments/assets/a439d79f-f9fd-484f-bff4-21a2146ab62f" />

<img width="795" height="153" alt="image" src="https://github.com/user-attachments/assets/081be397-83e4-4ca8-b002-b076c538ab55" />

<img width="766" height="162" alt="image" src="https://github.com/user-attachments/assets/8b64b56f-13ca-40a4-b7ca-e52d67c0987f" />

<img width="844" height="232" alt="image" src="https://github.com/user-attachments/assets/7dd87989-1090-48da-8797-352cb647d774" />

<img width="680" height="273" alt="image" src="https://github.com/user-attachments/assets/7ac66d22-e6e5-4fda-89e4-7b6c5525c194" />


The assignment objective is to build a real-time pipeline that captures simulated e-commerce inventory events, processes them, and updates DynamoDB with the latest inventory state.

<img width="673" height="306" alt="image" src="https://github.com/user-attachments/assets/c96c9b4c-a983-48f8-b885-5c69f6aed6ac" />

The generator sends events like product_added, product_removed, and product_quantity_changed into Kinesis every second. The Lambda currently handles product_added with put_item() and product_removed with delete_item() against the DynamoDB table product_inventory.

<img width="340" height="231" alt="image" src="https://github.com/user-attachments/assets/65894fc6-b1b9-4522-835b-9118ceb977c8" />

**Step-by-step execution**
**Step 1 — Create DynamoDB table**

Go to AWS Console. Search DynamoDB
- Click Tables
- Click Create table

- Table name: **product_inventory**
- Partition key: product_id
- Type: String
- Leave default settings

Click Create table

Lets explain this in detail.

*Step 1 — Create the DynamoDB Table (product_inventory)*

*1. Sign in to AWS Console*

Open: AWS Management Console. Enter your AWS account credentials and log in.

*2. Open DynamoDB*

At the top of the AWS Console: Click the Search bar
- Type: DynamoDB

Click DynamoDB from the search results. You will arrive at the DynamoDB Dashboard.

*3. Go to Tables*

In the left navigation menu:

```text
DynamoDB
│
├── Dashboard
├── Tables   ← Click here
├── Explore items
├── Streams
└── Exports
```

Click Tables.

*4. Click Create Table*

On the Tables page: Look at the top-right corner. Click the orange button:
- Create table

*5. Enter Table Name*

You will see the Create Table screen.

Under: Table details. Enter:
- Table name: **product_inventory**

Exactly as shown.

*6. Configure Partition Key*

Under: Partition key. Enter:
- product_id

For the data type select:
- String

Your screen should look similar to:

```text
Table name
─────────────────────
product_inventory

Partition key
─────────────────────
product_id    (String)
```

*7. Leave Sort Key Empty*

You will see: Add sort key (optional). Do NOT enable it. Leave it empty.

The Lambda function only uses:

<img width="272" height="92" alt="image" src="https://github.com/user-attachments/assets/35acd21d-3c23-4aaf-b78f-e9557b7a4958" />

so only the partition key is required.

*8. Select Capacity Mode*

Scroll down to: Table settings
- Choose: On-demand

This is the easiest option for the assignment.

You do not need to configure read/write capacity units.

*9. Keep Everything Else Default*

Leave:
- Encryption
- Backups
- Streams
- Tags
- Global tables

with their default settings.

*10. Create Table*

Scroll to the bottom. Click: Create table

AWS will begin creating the table.

*11. Wait Until Status Becomes Active*

You will return to the Tables page.

Initially you will see:
- Status -> Creating

Wait about 10–30 seconds. Refresh if necessary.

When it changes to:
- Status -> Active

the table is ready.

*12. Verify the Table*

Click: **product_inventory**

You should see:
- Table name: **product_inventory**
- Partition key: product_id (String)

Status: Active



