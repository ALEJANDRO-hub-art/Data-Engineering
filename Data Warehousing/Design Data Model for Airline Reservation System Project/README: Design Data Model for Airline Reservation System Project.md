I have the following project **Design Data Model for Airline Reservation System Project**

<img width="669" height="281" alt="image" src="https://github.com/user-attachments/assets/eacd58fe-54d0-477d-945c-4c6972fd1a73" />

# Airline Reservation System Data Model Project

## Goal
Design an optimized **reservation analytics model** for bookings, passengers, flights, aircraft, routes, airports, seats, payments, cancellations, loyalty, revenue, occupancy, route performance, and delay analysis.

## Main Grain
- `reservations`: one passenger booking/reservation.
- `tickets`: one passenger-seat-flight ticket.
- `flight_instances`: one scheduled flight occurrence.

## Suggested Execution Order
1. Run `schema.sql`.
2. Load airports, aircraft, routes, flights, customers/passengers.
3. Load reservations, tickets, payments, cancellations, loyalty transactions.
4. Run `insight_queries.sql`.
5. Use the provided ER diagram files in the solution.

----------------------------------------------------------------------------------------------------------------------------------

What each file does:

<img width="721" height="428" alt="image" src="https://github.com/user-attachments/assets/a8125968-dd1b-46ad-87a2-1011454d8a39" />

<img width="470" height="319" alt="image" src="https://github.com/user-attachments/assets/843c1c66-52b5-4949-925a-0b8ef90f21fe" />

**MySQL GUI execution steps**

Use MySQL Workbench.

*Step 1: Open MySQL Workbench*

Open MySQL Workbench.
- Click your local connection, usually Local instance MySQL80.
- Enter your MySQL password.
 
Click OK.

*Step 2: Create the database*

Click the SQL + button to open a new query tab.

Run:

- CREATE DATABASE airline_reservation_db;
- USE airline_reservation_db;

Click the yellow lightning icon.

*Step 3: Run schema.sql*

Go to File → Open SQL Script.

Select:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\11 Data Warehousing\Module 8 - Class 2\2 Class Assignment & Solution\Data_Modelling_Assignment_Solution\3 Design Data Model for Airline Reservation Syste

Click Open.

Make sure this line is at the top: USE airline_reservation_db; Click the yellow lightning icon to execute.

On the left panel, right-click Schemas. Click Refresh All. Expand airline_reservation_db → **Tables.**

You should see tables like:
- airports
- aircraft
- routes
- flights
- flight_instances
- customers
- passengers
- reservations
- fare_classes
- tickets
- payments
- cancellations
- loyalty_transactions

*Step 4: Load data*

Your uploaded CSV file is only a dictionary template, not real table data. So for this project, you either need to manually insert sample records or create CSVs for each table.

Correct loading order:
- 1. airports
- 2. aircraft
- 3. routes
- 4. flights
- 5. flight_instances
- 6. customers
- 7. passengers
- 8. fare_classes
- 9. reservations
- 10. tickets
- 11. payments
- 12. cancellations
- 13. loyalty_transactions

This order matters because child tables depend on parent tables.

















