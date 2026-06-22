import pandas as pd
import plotly.express as px
import streamlit as st
from snowflake.connector import connect

st.set_page_config(page_title="Movies CDC Dashboard", layout="wide")
st.title("🎬 Movies CDC Dynamic Tables Dashboard")
st.caption("Snowflake Streams + Tasks + Dynamic Tables + Streamlit")


def get_connection():
    return connect(
        account=st.secrets["snowflake"]["account"],
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        warehouse=st.secrets["snowflake"].get("warehouse", "COMPUTE_WH"),
        database=st.secrets["snowflake"].get("database", "MOVIES_CDC_DB"),
        schema=st.secrets["snowflake"].get("schema", "MOVIES_CDC_SCHEMA"),
        role=st.secrets["snowflake"].get("role", None),
    )


@st.cache_data(ttl=60)
def load_data():
    query = """
        SELECT
            booking_id,
            customer_id,
            movie_id,
            booking_date,
            status,
            ticket_count,
            ticket_price,
            total_amount,
            change_action,
            is_update,
            change_timestamp,
            booking_status_category,
            booking_size_category,
            price_category,
            active_revenue,
            lost_revenue,
            is_valid_booking,
            booking_hour,
            booking_day_name,
            booking_day
        FROM movie_bookings_filtered
        ORDER BY booking_date DESC
    """
    with get_connection() as conn:
        return pd.read_sql(query, conn)


try:
    df = load_data()
except Exception as exc:
    st.error("Could not connect to Snowflake or read the dynamic table.")
    st.info("Check .streamlit/secrets.toml and confirm the SQL setup script ran successfully.")
    st.exception(exc)
    st.stop()

if df.empty:
    st.warning("No data found yet. Run the SQL setup script and execute the task once.")
    st.stop()

# Normalize dates
for col in ["BOOKING_DATE", "CHANGE_TIMESTAMP", "BOOKING_DAY"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col])

st.sidebar.header("Filters")
min_date = df["BOOKING_DATE"].min().date()
max_date = df["BOOKING_DATE"].max().date()
date_range = st.sidebar.date_input("Booking date range", [min_date, max_date])

statuses = ["All"] + sorted(df["STATUS"].dropna().unique().tolist())
selected_status = st.sidebar.selectbox("Booking status", statuses)

movies = ["All"] + sorted(df["MOVIE_ID"].dropna().unique().tolist())
selected_movie = st.sidebar.selectbox("Movie", movies)

filtered = df.copy()
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        (filtered["BOOKING_DATE"].dt.date >= start_date)
        & (filtered["BOOKING_DATE"].dt.date <= end_date)
    ]
if selected_status != "All":
    filtered = filtered[filtered["STATUS"] == selected_status]
if selected_movie != "All":
    filtered = filtered[filtered["MOVIE_ID"] == selected_movie]

if st.sidebar.button("Refresh data"):
    st.cache_data.clear()
    st.rerun()

metric1, metric2, metric3, metric4, metric5 = st.columns(5)
metric1.metric("Total bookings", f"{len(filtered):,}")
metric2.metric("Tickets", f"{int(filtered['TICKET_COUNT'].sum()):,}")
metric3.metric("Active revenue", f"${filtered['ACTIVE_REVENUE'].sum():,.2f}")
metric4.metric("Lost revenue", f"${filtered['LOST_REVENUE'].sum():,.2f}")
quality = filtered["IS_VALID_BOOKING"].mean() * 100 if len(filtered) else 0
metric5.metric("Quality score", f"{quality:.1f}%")

left, right = st.columns(2)

with left:
    st.subheader("Revenue by status")
    revenue_by_status = (
        filtered.groupby("STATUS", as_index=False)[["ACTIVE_REVENUE", "LOST_REVENUE"]].sum()
    )
    revenue_long = revenue_by_status.melt(
        id_vars="STATUS", value_vars=["ACTIVE_REVENUE", "LOST_REVENUE"],
        var_name="Revenue Type", value_name="Revenue"
    )
    st.plotly_chart(px.bar(revenue_long, x="STATUS", y="Revenue", color="Revenue Type", barmode="group"), use_container_width=True)

with right:
    st.subheader("Booking status distribution")
    status_counts = filtered.groupby("STATUS", as_index=False).size()
    st.plotly_chart(px.pie(status_counts, names="STATUS", values="size"), use_container_width=True)

st.subheader("Movie performance")
movie_perf = (
    filtered.groupby("MOVIE_ID", as_index=False)
    .agg(
        bookings=("BOOKING_ID", "count"),
        tickets=("TICKET_COUNT", "sum"),
        active_revenue=("ACTIVE_REVENUE", "sum"),
        lost_revenue=("LOST_REVENUE", "sum"),
        avg_ticket_price=("TICKET_PRICE", "mean"),
    )
    .sort_values("active_revenue", ascending=False)
)
st.dataframe(movie_perf, use_container_width=True)

st.subheader("Bookings by hour")
hourly = filtered.groupby("BOOKING_HOUR", as_index=False).size().sort_values("BOOKING_HOUR")
st.plotly_chart(px.line(hourly, x="BOOKING_HOUR", y="size", markers=True), use_container_width=True)

st.subheader("Filtered raw data")
st.dataframe(filtered, use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download filtered CSV",
    data=csv,
    file_name="movie_bookings_filtered_export.csv",
    mime="text/csv",
)
