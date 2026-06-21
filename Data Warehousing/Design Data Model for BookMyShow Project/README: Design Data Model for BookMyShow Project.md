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
























