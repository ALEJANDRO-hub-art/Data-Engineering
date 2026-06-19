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

<img width="657" height="340" alt="image" src="https://github.com/user-attachments/assets/09653ced-5238-4a45-84c9-a1a560a44409" />


























