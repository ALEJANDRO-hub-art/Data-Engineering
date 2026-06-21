# BookMyShow Data Model Project

## Goal
Design a relational analytics data model for movie/event booking insights such as popular genres by location, 
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
