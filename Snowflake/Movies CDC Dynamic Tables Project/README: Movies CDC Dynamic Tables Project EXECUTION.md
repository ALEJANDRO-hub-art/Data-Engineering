I have this project Movies CDC Dynamic Tables Project EXECUTION.

<img width="869" height="298" alt="image" src="https://github.com/user-attachments/assets/e587bf1c-1151-4dac-8e02-4958f28bbfa8" />

<img width="864" height="156" alt="image" src="https://github.com/user-attachments/assets/b98b701b-8376-4e62-b8cc-dfaa44d14dec" />

<img width="826" height="156" alt="image" src="https://github.com/user-attachments/assets/185fb138-4b6b-41fe-8c26-c3c07cc4d400" />

<img width="825" height="155" alt="image" src="https://github.com/user-attachments/assets/cc7ab8f4-b81e-4837-a884-64cb80df9291" />

<img width="880" height="158" alt="image" src="https://github.com/user-attachments/assets/c739b521-af84-4734-930b-46a990b719be" />

<img width="831" height="186" alt="image" src="https://github.com/user-attachments/assets/fe88d31a-f192-41b8-9494-3317ba0897b8" />

This is a **Snowflake CDC + Dynamic Tables + Streamlit** dashboard project. It captures movie booking changes using Snowflake Streams/Tasks, transforms them with Dynamic Tables, then displays KPIs in Streamlit.

**File upload locations**

<img width="689" height="439" alt="image" src="https://github.com/user-attachments/assets/31870085-1b0e-4683-a125-cf59eebbb64a" />

**Snowflake GUI execution steps**

*Step 1 — Run main setup SQL*

Log in to Snowflake. Left menu → click Projects. Click Worksheets. Click + Worksheet.

Open **snowflake_dynamic_tables.sql**. Copy all SQL code. Paste it into the worksheet.
- Click Run All.
- Wait until it finishes.

In Object Explorer, confirm database:
- **MOVIES_CDC_DB**

Open:
- **MOVIES_CDC_DB → MOVIES_CDC_SCHEMA**

Confirm these objects exist:
- raw_movie_bookings
- movie_bookings_stream
- movie_booking_cdc_events
- consume_stream_task
- movie_bookings_filtered
- movie_booking_insights

These are the expected Snowflake objects for the project.

In this **snowflake_dynamic_tables.sql** file we do the following:
- Create database (**MOVIES_CDC_DB**) and schema (**MOVIES_CDC_SCHEMA**)
- USE WAREHOUSE **COMPUTE_WH**
- CREATE **raw_movie_bookings** and insert values
- CREATE **movie_bookings_stream**
- CREATE **movie_booking_cdc_events**
- CREATE **consume_stream_task** and insert values
- CREATE **movie_bookings_filtered**
- CREATE **movie_booking_insights**
- Helpful verification commands - SHOW TABLES; SHOW STREAMS; SHOW TASKS; SHOW DYNAMIC TABLES;

**Test CDC changes in Snowflake GUI**

Create a new Snowflake worksheet. Open:
- **test_cdc_changes.sql.**
 
Copy the code. Paste it into the worksheet. Click Run All.

This test script inserts one booking, cancels one booking, deletes one booking, executes the task, refreshes the dynamic tables, and shows final SELECT results.

Lets inspect this **test_cdc_changes.sql.** file and whats in it:
- Insert values into **raw_movie_bookings**
- In **raw_movie_bookings** update an existing booking to CANCELLED
- In **raw_movie_bookings** delete a booking
- Force the task to consume the stream immediately: 'EXECUTE TASK **consume_stream_task**';
- Refresh dynamic tables manually
- Check Results

**Monitor the pipeline**

Create another Snowflake worksheet. Open:
- **monitoring_queries.sql.**

Run each query one by one. Use the results to check:
- Task history
- Stream status
- Dynamic table refresh status
- Recent CDC events


















