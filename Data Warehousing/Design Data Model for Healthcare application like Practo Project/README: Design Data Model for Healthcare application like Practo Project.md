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

Lets inspect this **schema.sql** file:

This code creates a healthcare appointment database schema.

It builds tables to store:

1. Locations
- Stores city, area, and state information.

2. Patients
- Stores patient details like name, email, phone, signup date, gender, date of birth, and their location.

3. Specialties
- Stores medical specialties, such as cardiology, dermatology, dentistry, etc.

4. Doctors
- Stores doctor details, including specialty, years of experience, and consultation fee.

5. Clinics
- Stores clinic names and their locations.

6. Doctor-clinic relationship
- doctor_clinics connects doctors to clinics. This allows one doctor to work in multiple clinics and one clinic to have many doctors.

7. Marketing campaigns
- Stores campaign details like campaign name, channel, dates, and cost.

8. Appointments
- Stores appointment bookings between patients, doctors, and clinics. It also tracks campaign source, booking time, appointment time, status, type, fee, and discount.

9. Consultations
- Stores consultation details after an appointment, including start/end time, diagnosis summary, and whether follow-up is required.

10. Prescriptions
- Stores prescriptions created from consultations.

11. Prescription items
- Stores individual medicines inside each prescription, including medicine name, dosage, and duration.

12. Payments
- Stores payment details for appointments, including method, status, timestamp, and paid amount.

13. Reviews
- Stores patient reviews for doctors and appointments, including rating, review text, and review time.

14. Cancellations
- Stores cancelled appointments, who cancelled them, reason, cancellation time, and refund amount.

Overall, this schema models the full workflow of a healthcare app like Practo:
- **patient signup → doctor/clinic selection → appointment booking → consultation → prescription → payment → review or cancellation.**

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

Lets inspect this **insight_queries.sql**.

This SQL code runs 10 healthcare analytics reports on the database.

1. Most booked specialties by location
- Shows which doctor specialties get the most appointments in each city and area.

2. Doctor utilization / appointment volume
- Shows how many completed appointments each doctor handled. Doctors with zero completed appointments still appear because of the LEFT JOIN.

3. Average consultation fee by specialty
- Calculates the average doctor consultation fee for each specialty.

4. Appointment cancellation rate
- Calculates the percentage of all appointments that were cancelled.

5. Average patient wait time
- Calculates each doctor’s average wait time in minutes, from scheduled appointment time to consultation start time.

7. Revenue by doctor and clinic
- Shows total successful payment revenue for each doctor at each clinic.

9. Monthly new patient acquisition
- Counts how many new patients signed up each month.

10. Campaign effectiveness
- Shows each marketing campaign’s engaged patients and successful payment revenue. Campaigns with no revenue still appear.

11. Doctor ratings
- Shows each doctor’s average rating and number of reviews. Doctors with no reviews still appear.

12. Follow-up requirement rate by specialty
- Calculates the percentage of consultations that required follow-up for each specialty.

Overall, these queries analyze:
appointments, doctor performance, fees, cancellations, wait times, revenue, patient growth, marketing campaigns, ratings, and follow-up needs.






















