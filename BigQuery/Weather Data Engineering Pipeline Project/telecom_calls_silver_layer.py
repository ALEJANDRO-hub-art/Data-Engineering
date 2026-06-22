# Converted from Jupyter Notebook
# Source notebook: telecom_calls_silver_layer(5).ipynb


# %%
# 1) Imports & constants
import bigframes.pandas as bf
from google.cloud import bigquery

PROJECT   = "mythic-aloe-457912-d5"
DATASET   = "telecom_db"
BRONZE    = f"{PROJECT}.{DATASET}.telecom_data_transformed"
SILVER    = f"{PROJECT}.{DATASET}.telecom_calls_silver_v1"

# 2) Read your Bronze table (force latest, bypass cache)
bronze = bf.read_gbq(BRONZE, use_cache=False)

# 3) Clean, cast, enrich
silver = (
    bronze
    # drop any rows missing our core IDs & metrics
    .dropna(subset=["call_id", "duration_seconds", "data_usage_mb"])
    # cast to safe BigFrames dtypes
    .assign(
        call_date=lambda df: bf.to_datetime(df["call_date"]),
        duration_seconds=lambda df: df["duration_seconds"].astype("Int64"),
        data_usage_mb=lambda df: df["data_usage_mb"].astype("Float64"),
    )
)

silver.head(20)

# %%
# 4) Pre-create your Silver table with partitioning & clustering
client = bigquery.Client(project=PROJECT)
table_id = SILVER

try:
    client.get_table(table_id)  # Check if table exists
    print(f"Table {table_id} already exists.")
except Exception as e:
    schema = [
        bigquery.SchemaField("call_id",          "STRING"),
        bigquery.SchemaField("customer_id",      "STRING"),
        bigquery.SchemaField("driver_id",        "STRING"),  # Include driver_id
        bigquery.SchemaField("call_date",        "TIMESTAMP"),
        bigquery.SchemaField("duration_seconds", "INT64"),
        bigquery.SchemaField("call_type",        "STRING"),
        bigquery.SchemaField("data_usage_mb",    "FLOAT64"),
        bigquery.SchemaField("region",           "STRING"),
        bigquery.SchemaField("plan_type",        "STRING"),
    ]
    table = bigquery.Table(table_id, schema=schema)

    # partition by DATE(call_date)
    table.time_partitioning = bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="call_date",
    )
    # cluster by region & plan_type
    table.clustering_fields = ["region", "plan_type"]
    client.create_table(table, exists_ok=True)
    print(f"Table {table_id} created.")

# %%
# 5) Append your Silver DataFrame into that table
silver.to_gbq(
    destination_table=SILVER,
    if_exists="replace",
)
