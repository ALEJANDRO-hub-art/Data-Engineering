# Converted from Jupyter Notebook
# Source notebook: telecom_calls_gold(5).ipynb


# %%
# 1) Imports & clients
import bigframes.pandas as bf
from google.cloud import bigquery

PROJECT   = "mythic-aloe-457912-d5"
DATASET   = "telecom_db"
SILVER_TB = f"{PROJECT}.{DATASET}.telecom_calls_silver_v1"
GOLD_TB   = f"{PROJECT}.{DATASET}.telecom_calls_gold_v1"

bq = bigquery.Client(project=PROJECT)

# 2) Ensure your Gold table exists (idempotent DDL)
ddl = f"""
CREATE TABLE IF NOT EXISTS `{GOLD_TB}` (
  date           DATE,
  region         STRING,
  plan_type      STRING,
  total_calls    INT64,
  avg_duration   FLOAT64,
  total_duration INT64,
  avg_data_mb    FLOAT64,
  total_data_mb  FLOAT64
)
PARTITION BY date
CLUSTER BY region, plan_type
OPTIONS (
  description = "Daily telecom KPIs by region & plan",
  labels = [("layer","gold"),("team","dataeng")]
)
"""
bq.query(ddl).result()  # blocks until done

# %%
# 3) Read your Silver table from BigQuery
#    use_cache=False to always hit the latest
silver = bf.read_gbq(SILVER_TB, use_cache=False)

# 4) Derive a pure DATE column and aggregate
gold_df = (
    silver
    # make sure call_date is a timestamp, then pull out its date()
    .assign(
        call_ts = lambda df: bf.to_datetime(df["call_date"]),
        date    = lambda df: df["call_ts"].dt.date  # DATE
    )
    # group & compute KPIs
    .groupby(["date", "region", "plan_type"])
    .agg(
        total_calls    = ("call_id",        "count"),
        avg_duration   = ("duration_seconds","mean"),
        total_duration = ("duration_seconds","sum"),
        avg_data_mb    = ("data_usage_mb",   "mean"),
        total_data_mb  = ("data_usage_mb",   "sum"),
    )
    .reset_index()
)

gold_df.head(5)

# %%
# 5) Load aggregated DataFrame back into the Gold table
#    We turn the BigFrame into an in-runtime pandas DF for loading,
#    but since the work was pushed down, it's still efficient.
to_load = gold_df.to_pandas()

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE",  # replace partition/day
    time_partitioning=bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="date",
    ),
    clustering_fields=["region", "plan_type"],
)

load_job = bq.load_table_from_dataframe(
    to_load,
    GOLD_TB,
    job_config=job_config,
    # you can set job_id_prefix or location here if needed
)
load_job.result()  # wait for completion

print(f"Loaded {load_job.output_rows} rows into {GOLD_TB}")

# %%
