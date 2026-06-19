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


























