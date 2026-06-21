I have this project Design Data Model for Healthcare application like Practo Project.

<img width="835" height="282" alt="image" src="https://github.com/user-attachments/assets/3bb9f7a9-438c-464e-8316-68539f0853b8" />

Project name: **Healthcare / Practo Data Model Project**

Brief explanation of each file

<img width="706" height="361" alt="image" src="https://github.com/user-attachments/assets/59728549-1942-40c8-a78f-23fc3b12511f" />

<img width="623" height="356" alt="image" src="https://github.com/user-attachments/assets/5f090a59-491f-4dfb-b53e-437a24835eec" />

**Step-by-step execution in MySQL Workbench GUI**

*Step 1: Open MySQL Workbench*

Open MySQL Workbench.
 
Click your local connection, for example: Local instance MySQL80

*Step 2: Create the database*

Click the SQL editor and run:
- CREATE DATABASE healthcare_practo_db;
- USE healthcare_practo_db;

Click the lightning bolt icon to execute.

*Step 3: Open and run schema.sql*

In MySQL Workbench: File → Open SQL Script
- Select: **schema.sql**

Click the lightning bolt icon.

This creates all tables.

*Step 4: Confirm tables were created*

On the left panel: **Schemas → healthcare_practo_db → Tables**

Right-click Tables → Refresh All.

You should see tables like:
- locations
- patients
- doctors
- clinics
- appointments
- consultations
- prescriptions
- payments
- reviews
- cancellations

*Step 5: Load data*

This project currently has schema and queries, but I do not see actual insert/sample data rows in the CSV. So you may need to manually insert data or generate sample data.

To insert sample data, open a new SQL tab and use INSERT INTO statements.

Example:

<img width="475" height="198" alt="image" src="https://github.com/user-attachments/assets/7b7a857b-397a-49f6-bb69-aa5848e0db56" />

*Step 6: Run analytics queries*

Open: File → Open SQL Script

Select: **insight_queries.sql**

Run each query one by one.

Important: your insight_queries.sql looks written more for PostgreSQL, not pure MySQL. Some functions may fail in MySQL, such as:

<img width="357" height="105" alt="image" src="https://github.com/user-attachments/assets/3edbb1a4-06ca-4b10-ab56-f8adddd977eb" />

For MySQL, replace them with:

<img width="421" height="90" alt="image" src="https://github.com/user-attachments/assets/17a90ae9-e72d-4348-913b-2219fd38a029" />



