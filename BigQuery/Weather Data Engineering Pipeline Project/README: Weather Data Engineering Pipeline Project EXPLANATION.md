# 🚀 BigQuery & Google Cloud Data Engineering Portfolio 

> **This is NOT a single project.**
>
> It is a collection of **6 different Google Cloud, BigQuery, and Data Engineering mini-projects** designed to teach progressively advanced concepts in modern data engineering.

---

# 📖 Big Picture

This repository contains multiple projects that progress from:

✅ Basic BigQuery Tables
✅ External Tables
✅ Analytics Datasets
✅ Streaming Pipelines
✅ Medallion Architecture
✅ Production-Grade Weather Pipeline with Airflow, Spark, CI/CD, and Cloud Storage

Think of this repository as a **BigQuery & Google Cloud Data Engineering Learning Portfolio**, where each folder teaches a different real-world data engineering concept.

---

# 🏗️ Learning Path

```text
1. Managed Tables
        ↓
2. External Tables
        ↓
3. Analytics Dataset
        ↓
4. Streaming Pipeline
        ↓
5. Medallion Architecture
        ↓
6. Production Weather Pipeline
```

---

# 📁 Project 1: Managed Tables in BigQuery

## Folder

```text
1 Managed-Tables-BQ
```

## 🎯 What It Does

This is the most basic BigQuery project.

### Workflow

```text
CSV File
    ↓
Google Cloud Storage
    ↓
BigQuery Table
    ↓
Daily Summary Table
    ↓
Scheduled Query
```

## 📄 Files

### `commands.sql`

Creates:

* Dataset
* Tables
* CSV Data Loads

### `scheduled_query.sql`

Creates automated daily aggregations.

## 🧠 What You Learn

* BigQuery Datasets
* Native BigQuery Tables
* Scheduled Queries
* Data Aggregation
* Data Warehousing Fundamentals

## 🌎 Real-World Example

A telecom company loads call records into BigQuery daily and generates KPI reports automatically.

---

# 📁 Project 2: External Tables in BigQuery

## Folder

```text
2 External-Tables-BQ
```

## 🎯 What It Does

Instead of loading data into BigQuery, BigQuery reads JSON files directly from Cloud Storage.

### Workflow

```text
JSON Files
      ↓
Google Cloud Storage
      ↓
External Table
      ↓
BigQuery Queries
```

## 📄 Files

### `create_bq_external_table.sql`

Creates:

* Dataset: `lyft_db`
* External Table

Pointing to:

```text
gs://bigquery-data-gds/raw/date=*
```

## 🧠 What You Learn

* External Tables
* Querying Files Without Loading Data
* Data Lake Concepts
* Cloud Storage Integration

## 🌎 Real-World Example

Lyft or Uber ride files arrive daily in Cloud Storage and are queried directly by analysts.

---

# 📁 Project 3: Starbucks Data Analytics

## Folder

```text
3 BQ-Data-Canvas-Dataset
```

## 📄 Files

* `starbucks_customers.csv`
* `starbucks_transaction.csv`

## 🎯 What It Does

A pure analytics project focused on customer and transaction analysis.

### Workflow

```text
Customer Data
      +
Transaction Data
      ↓
BigQuery
      ↓
Analytics
      ↓
Dashboards
```

## 📊 Example Business Questions

* Top Customers
* Revenue by Store
* Revenue by Month
* Loyalty Trends
* Customer Spending Patterns

## 🧠 What You Learn

* Data Modeling
* SQL Analytics
* Analytical Data Sets
* Dashboard Design Preparation

---

# 📁 Project 4: Streaming Pipeline

## Folder

```text
4 LoyaltyProgram-PubSub-Stream-To-BigQuery-Project
```

## 🎯 What It Does

This is the first real-time streaming pipeline in the portfolio.

## 🏗️ End-to-End Architecture

```text
Python Generator
        ↓
Pub/Sub
        ↓
Dataflow
        ↓
Transform UDF
        ↓
BigQuery
```

---

## 📄 File 1: `mock_data_to_pubsub.py`

Creates fake customer events such as:

* New Customer
* Purchase
* Reward Earned
* Membership Update

Publishes events to Google Pub/Sub.

---

## 📄 File 2: `transform_udf.py`

Performs transformations such as:

* Lowercase Email
* Name Formatting
* Timestamp Standardization
* Loyalty Status Calculation
* Account Age Calculation

---

## 📄 File 3: `bigquery_create_table.sql`

Creates the destination BigQuery table used to store transformed events.

---

## 🧠 What You Learn

* Streaming Pipelines
* Google Pub/Sub
* Dataflow
* Event Processing
* Real-Time Analytics

## 🌎 Real-World Example

A Starbucks Rewards Program processing customer activity in real time.

---

# 📁 Project 5: Telecom Medallion Architecture

## Folder

```text
5 TelecomPipelineInBQ2
```

## 🎯 What It Does

This project teaches the industry-standard **Medallion Architecture** pattern.

## 🏗️ Architecture

```text
RAW
 ↓
SILVER
 ↓
GOLD
```

---

## 📄 Silver Layer Notebook

### `telecom_calls_silver_layer.ipynb`

Reads raw telecom data and performs:

* Null Handling
* Data Type Fixes
* Column Formatting
* Data Validation
* Data Cleansing

### Output

```text
Silver Table
```

---

## 📄 Gold Layer Notebook

### `telecom_calls_gold.ipynb`

Reads Silver Layer data and creates:

* KPIs
* Revenue Metrics
* Customer Metrics
* Usage Metrics
* Trend Analysis

### Output

```text
Gold Tables
```

---

## 🧠 What You Learn

* Data Lakehouse Concepts
* ETL Processing
* Medallion Architecture
* Analytics Engineering

## 🌎 Real-World Example

A telecom call-center analytics platform.

---

# 📁 Project 6: Weather Data Processing (Most Advanced)

## Folder

```text
6 weather-data-processing
```

## 🎯 What It Does

This is the most advanced and production-ready project in the entire collection.

The architecture demonstrates a complete weather data pipeline using:

* Weather API
* Python
* Cloud Storage
* Apache Spark
* Apache Airflow
* CI/CD
* Data Warehouse Technologies

---

## 🏗️ High-Level Architecture

```text
Weather API
      ↓
Python
      ↓
Cloud Storage
      ↓
Spark Processing
      ↓
Data Warehouse

Orchestrated By:

Apache Airflow
```

---

## 📄 `weather_data_processing.py`

### Spark ETL Job

Performs:

* Read Weather Data
* Transform
* Clean
* Aggregate
* Load

---

## 📄 `extract_data_dag.py`

### Airflow DAG

Responsible for:

* API Extraction
* Scheduling
* Workflow Automation

---

## 📄 `transform_data_dag.py`

### Airflow DAG

Responsible for:

* Data Transformations
* Loading Processed Data

---

## 📄 `ci-cd.yaml`

### GitHub Actions Pipeline

Automates:

* Testing
* Validation
* Deployment

---

## 🧠 What You Learn

* Apache Spark
* Apache Airflow
* GitHub Actions
* CI/CD Pipelines
* Cloud Storage
* Production Data Engineering

---

# 🎓 Overall Summary

This repository represents a complete **Google Cloud & BigQuery Data Engineering Learning Path**.

```text
Managed Tables
      ↓
External Tables
      ↓
Analytics Datasets
      ↓
Streaming Pipelines
      ↓
Medallion Architecture
      ↓
Production Data Engineering
```

By completing all six projects, you gain hands-on experience with:

✅ BigQuery
✅ Google Cloud Storage (GCS)
✅ Pub/Sub
✅ Dataflow
✅ Apache Spark
✅ Apache Airflow
✅ GitHub Actions
✅ CI/CD Pipelines
✅ Medallion Architecture
✅ Analytics Engineering
✅ Production-Ready Data Pipelines

🚀 Together, these projects form a practical Data Engineering portfolio demonstrating skills ranging from foundational BigQuery concepts to enterprise-grade cloud data pipelines.






















