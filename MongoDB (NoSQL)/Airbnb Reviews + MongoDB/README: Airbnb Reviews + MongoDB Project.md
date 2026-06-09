We have the Airbnb Reviews + MongoDB Project.

<img width="687" height="210" alt="image" src="https://github.com/user-attachments/assets/ccf641a9-ecd1-44f4-a655-ebd02bdbbb8a" />

<img width="624" height="334" alt="image" src="https://github.com/user-attachments/assets/a10ed6cc-9403-42c3-b470-4061395eeaf8" />

The **mongo_connect.py** file doesnt load **airbnb_reviews.json**; it assumes the JSON data is already stored inside MongoDB. In other words **mongo_connect.py** is not a loader its a **query / analytics script**.

✅ What the script actually does
✔ Connects to MongoDB Atlas

<img width="296" height="87" alt="image" src="https://github.com/user-attachments/assets/027b47d2-3493-4ea9-a865-3105bed95dd2" />

✔ Selects database + collection

<img width="311" height="106" alt="image" src="https://github.com/user-attachments/assets/02be17f9-220e-476b-9ff0-650fae56fe73" />

❌ Does NOT insert any JSON file. (Your instructor commented out insert lines)
✔ Runs a MongoDB aggregation

<img width="358" height="103" alt="image" src="https://github.com/user-attachments/assets/c9628a49-0dbe-46e3-a7e6-55b88aa9edf2" />

✔ Prints the results of the aggregation
It does analytics like:

- Group by country + suburb
- Compute average price

🧩 Here's how to load **airbnb_reviews.json**

Create a NEW script in the same folder: **load_reviews.py**

Paste this code 👇

<img width="614" height="437" alt="image" src="https://github.com/user-attachments/assets/303475a2-0829-46a1-8e2c-39c3913f1f64" />

<img width="668" height="122" alt="image" src="https://github.com/user-attachments/assets/be1c942f-ed00-452d-97eb-105ea3ebc7e8" />

💡 Why it's separated

Your course likely split the tasks:

| File | Purpose |
|------|---------|
| **airbnb_reviews.json** | Data snapshot of Airbnb listings |
| **load_reviews.py** (missing from folder) | Insert JSON into MongoDB |
| **mongo_connect.py** | Query & aggregate data AFTER it's imported |

🔥 What to do now

✅ Step 1 — Load JSON

Create **load_reviews.py** with the code above → **run it**

Verify MongoDB Compass shows hundreds/thousands of documents


✅ Step 2 — Run mongo_connect.py

<img width="213" height="67" alt="image" src="https://github.com/user-attachments/assets/d47c6c56-653d-40f6-9cba-1d9a9514ec2e" />

Now the aggregation queries will return results 🎉

<img width="668" height="540" alt="image" src="https://github.com/user-attachments/assets/256c0b2d-dfdd-48c1-88f3-571e81da340c" />

<img width="867" height="215" alt="image" src="https://github.com/user-attachments/assets/e5a73a69-c90f-4dfe-98cf-593c5d41d956" />

------------------------------------------------------------------------------------------------------

<img width="626" height="445" alt="image" src="https://github.com/user-attachments/assets/346073e3-be9d-4ff3-a356-f7ccedd24f5c" />

## Step-by-step GUI execution
**Step 1 — Open MongoDB Atlas**
- Go to:
  - MongoDB Atlas → Database → Browse Collections
- Create or select:
  - Database: airbnb
  - Collection: reviews

**Step 2 — Import the JSON file**
Open MongoDB Compass.
- Click:
  - New Connection
  - Paste your MongoDB Atlas connection string.
- Then go to:
  - airbnb → reviews → Add Data → Import JSON or CSV file
- Select: airbnb_reviews.json
- Choose: File Type: JSON
- Click: Import

**Step 3 — Verify data loaded**
In MongoDB Compass, check that **reviews** shows many documents.

**Step 4 — Put the Python file in your folder**
Keep this file in the same project folder:

<img width="602" height="162" alt="image" src="https://github.com/user-attachments/assets/547a0230-c6e4-42c4-838d-d691716da38c" />

<img width="596" height="147" alt="image" src="https://github.com/user-attachments/assets/5870a6a4-e2d2-48cc-b307-fb45b9bacaf8" />

The following is an explanation of Step 5

Open Command Prompt.

Type: **cd "C:\Users\Alejandro\Documents\6 MongoDB (NoSQL)\Module 4 - MongoDB Class 2\1 Class Content\Code_Files"**

Verify you're in the correct folder

Run: **dir**

You should see:
- airbnb_reviews.json
- mongo_connect.py
- ksql_db_commands.sql

<img width="629" height="228" alt="image" src="https://github.com/user-attachments/assets/c5dba729-809f-42fd-8df9-c7cdb6728001" />

<img width="597" height="107" alt="image" src="https://github.com/user-attachments/assets/60c99192-03ca-4c30-b47e-7cadfa808cfe" />










