I have this project Design Data Model for food delivery app like Zomato-Swiggy Project.

<img width="838" height="276" alt="image" src="https://github.com/user-attachments/assets/2eef0305-9aaa-4208-b339-199b3a6ebd85" />

This is a **Food Delivery App Data Model Project for a Zomato/Swiggy-style platform**. The goal is to design and run a relational analytics database for restaurants, menus, customers, orders, deliveries, payments, cancellations, cuisines, locations, and campaigns.

<img width="551" height="332" alt="image" src="https://github.com/user-attachments/assets/d0608734-fff9-4c23-8205-82df74bd82a7" />

**Step-by-step execution in MySQL Workbench GUI**

*Step 1: Create the database*

Open MySQL Workbench.

Click your MySQL connection. Click the SQL + icon to open a new query tab.

Run:
- CREATE DATABASE food_delivery_db;
- USE food_delivery_db;

Click the lightning bolt button.

*Step 2: Run the schema file*

Go to: File → Open SQL Script
- Select: **schema.sql**

Make sure the first line says:
- USE food_delivery_db;

If it does not, add it at the top.

Click the lightning bolt.

This creates tables like:
- locations, customers, restaurants, cuisines, menu_items, orders, order_items, payments, deliveries, and cancellations.

*Step 3: Load data*

Your CSV file looks like a data dictionary, not actual table data. So this project is mainly a **data model + analytics query project.**

If you later receive actual CSV data, load it in this order:
- locations
- customers
- restaurants
- cuisines
- restaurant_cuisines
- menu_items
- delivery_personnel
- marketing_campaigns
- orders
- order_items
- deliveries
- payments
- cancellations

This order matters because child tables depend on parent tables.

*Step 4: Run the insight queries*

Go to: File → Open SQL Script

Select: **INSIGH~1.SQL**

Make sure you are using:
- USE food_delivery_db;

Run each query one by one, or run the whole file.

These queries answer questions like:
- Most popular restaurants by location
- Busiest order times
- Average order value by customer
- Average delivery time
- Most ordered cuisines
- Cancellation rate
- Revenue by restaurant
- New customers by month
- Campaign revenue impact

*Step 5: View the ER diagram*

Open: **ER_DIA~1.PNG**

Use this image in your assignment/report.

It shows the project relationships:

<img width="847" height="277" alt="image" src="https://github.com/user-attachments/assets/df250bc7-56f9-487a-a492-1b55a3d86e4f" />

**End-to-end architecture**

<img width="475" height="247" alt="image" src="https://github.com/user-attachments/assets/2821658b-9fd1-422a-a084-f6efbdc2e6db" />




















