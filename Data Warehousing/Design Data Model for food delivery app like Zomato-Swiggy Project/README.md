# Food Delivery App Data Model Project

## Goal
Design a relational analytics model for a Zomato/Swiggy-style platform covering restaurants, menus, orders, delivery, cancellations, pricing, discounts, revenue, customers, locations, cuisines, and campaigns.

## Main Grain
- `orders`: one customer order.
- `order_items`: one menu item inside an order.
- `deliveries`: one delivery attempt per order.

## Suggested Execution Order
1. Run `schema.sql`.
2. Load locations, customers, restaurants, cuisines, menu items, delivery personnel, campaigns.
3. Load orders, order items, deliveries, payments/cancellations.
4. Run `insight_queries.sql`.
5. Attach `er_diagram.png` or `er_diagram.mmd` in your assignment.
