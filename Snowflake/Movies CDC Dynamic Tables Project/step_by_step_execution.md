# Step-by-step execution guide

## Part 1 — Download and unzip

1. Download the ZIP file.
2. Right-click it and choose **Extract All**.
3. Open the extracted folder: `movies_cdc_dynamic_tables_project`.

## Part 2 — Run Snowflake setup in the GUI

1. Log in to Snowflake.
2. In the left menu, click **Projects**.
3. Click **Worksheets**.
4. Click **+ Worksheet**.
5. Open the file `sql/snowflake_dynamic_tables.sql` from this project folder.
6. Copy all SQL code.
7. Paste it into the Snowflake worksheet.
8. Click **Run All**.
9. Wait until the script finishes.
10. In the Object Explorer, confirm the database `MOVIES_CDC_DB` was created.
11. Open `MOVIES_CDC_DB` → `MOVIES_CDC_SCHEMA`.
12. Confirm the tables, stream, task, and dynamic tables exist.

## Part 3 — Test CDC changes

1. Open a new Snowflake worksheet.
2. Open `sql/test_cdc_changes.sql`.
3. Copy and paste the code into the worksheet.
4. Click **Run All**.
5. This script inserts one booking, cancels one booking, deletes one booking, executes the task, and refreshes the dynamic tables.
6. Review the final SELECT results.

## Part 4 — Monitor the pipeline

1. Open a new Snowflake worksheet.
2. Open `sample_queries/monitoring_queries.sql`.
3. Run the queries one by one.
4. Use these results to check task history, stream status, dynamic table refresh status, and recent CDC events.

## Part 5 — Run Streamlit dashboard locally

1. Open Command Prompt or Anaconda Prompt.
2. Go into the extracted project folder.
3. Install packages:

```bash
pip install -r requirements.txt
```

4. Copy the secrets template:

```bash
copy .streamlit\secrets.toml.example .streamlit\secrets.toml
```

5. Open `.streamlit/secrets.toml` in Notepad.
6. Replace the Snowflake values with your real account, user, password, warehouse, database, schema, and role.
7. Run:

```bash
streamlit run app/streamlit_app.py
```

8. A browser tab opens with the dashboard.

## End-to-end workflow

```text
User inserts/updates/deletes movie booking rows
        ↓
Snowflake stream captures the changes
        ↓
Scheduled Snowflake task consumes the stream
        ↓
CDC events table stores raw changes and metadata
        ↓
Dynamic table adds business categories and revenue logic
        ↓
Analytics dynamic table aggregates insights
        ↓
Streamlit dashboard displays KPIs and charts
```
