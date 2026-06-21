I have this project Design Data Model for BookMyShow Project.

<img width="814" height="276" alt="image" src="https://github.com/user-attachments/assets/3d2cb777-7be7-44b8-a0b4-6995e861bdae" />

BookMyShow Data Model Project. It is a relational database design project for movie/event ticket booking analytics. The README says the goal is to model insights like popular genres, busiest booking times, cancellations, campaign performance, theatre revenue, and user acquisition.

Lets take a look at the the README file:

# BookMyShow Data Model Project

## Goal
Design a **relational analytics data model** for **movie/event booking insights** such as popular genres by location, 
busiest booking times, cancellations, campaign performance, pricing impact, theatre revenue, and user acquisition.

## Main Grain
- `bookings`: one booking transaction.
- `booking_items`: one ticket/item inside a booking.
- `payments`: one payment per booking attempt/payment event.

## Suggested Execution Order
1. Run `schema.sql` in PostgreSQL/MySQL-compatible SQL editor after minor type adjustments if needed.
2. Load source/application data into dimensions first: users, locations, theatres, screens, genres, movies, casts, campaigns.
3. Load transactional tables: bookings, booking_items, payments, cancellations.
4. Run `insight_queries.sql` for the required business questions.
5. Use `er_diagram.png` or `er_diagram.mmd` in the final solution document.

**Brief explanation of each file**

<img width="731" height="347" alt="image" src="https://github.com/user-attachments/assets/9f740906-c0fe-484d-a812-52c8e41b7212" />
 
Important note
- This project contains the data model and insight queries, but it does not appear to include INSERT/sample transaction data. So the schema can be created successfully, but the insight queries will return empty results until you insert or load sample data.

**Step-by-step execution in MySQL Workbench GUI**

*Step 1: Open MySQL Workbench*

Open MySQL Workbench.

Click your local connection, usually: Local instance MySQL80. Enter your password.

*Step 2: Create the database*

Click the SQL editor and run:
- CREATE DATABASE bookmyshow_db;
- USE bookmyshow_db;

Click the lightning bolt button to execute.

*Step 3: Open the schema file*

In MySQL Workbench: File → Open SQL Script

Select: **schema.sql**

Then run the full script using the lightning bolt.

This creates tables such as:
- locations
- users
- theatres
- screens
- genres
- movies
- events
- shows
- bookings
- booking_items
- payments
- cancellations

*Step 4: Check that tables were created*

On the left side, go to:
- Schemas → bookmyshow_db → Tables

Right-click Tables and click: Refresh All

You should see all project tables.

*Step 5: Open the insight queries file*

Go to: File → Open SQL Script
- Select: **insight_queries.sql**

Run one query at a time.

Examples of insights included:
- Popular genres by city
- Busiest booking hour/day
- Cancellation rate
- Average tickets per booking
- Campaign performance
- Revenue by theatre

**End-to-end workflow / architecture**

<img width="399" height="328" alt="image" src="https://github.com/user-attachments/assets/679d92ff-257e-4e99-b04c-dd64961bb476" />

Simple execution order
- 1 Create database: **bookmyshow_db**
- 2 Run **schema.sql**
- 3 Confirm tables were created
- 4 Load or insert sample data
- 5 Run **insight_queries.sql**
- 6 Use **er_diagram.png** in your final report

This is mainly a database design + analytics SQL project, not a full application GUI project.















