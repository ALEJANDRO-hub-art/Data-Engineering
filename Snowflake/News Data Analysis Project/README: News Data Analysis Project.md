I have this project News Data Analysis Project.

<img width="704" height="258" alt="image" src="https://github.com/user-attachments/assets/bcba7530-0ee0-4275-a510-69497e18ea7b" />

# 📰 News Data Analysis Project

## 📋 Project Overview

This project demonstrates a comprehensive **news data extraction and analysis pipeline** using **NewsAPI**, **Apache Airflow**, **Google Cloud Storage**, 
and **Snowflake**. The system automatically fetches news articles, processes them, and creates analytical tables for news source and author activity analysis.

## 🏗️ Architecture

<img width="739" height="131" alt="image" src="https://github.com/user-attachments/assets/ea1ede38-400a-4b06-9913-6073efe815b1" />

## 🎯 Key Features

- **🔄 Automated Data Extraction**: Daily news fetching with pagination support
- **📊 Real-time Processing**: Live news data from NewsAPI with comprehensive coverage
- **☁️ Cloud Integration**: Seamless GCS and Snowflake integration
- **🎛️ Airflow Orchestration**: Scheduled data pipeline with error handling
- **📈 Analytics Ready**: Pre-built summary tables for news source and author analysis
- **🔧 Schema Inference**: Automatic table creation from Parquet files
- **📝 Data Quality**: Content cleaning and validation

## 📁 Project Structure

<img width="606" height="111" alt="image" src="https://github.com/user-attachments/assets/5ad5d69e-27f0-436b-a7e8-37c8f8f761c0" />

## 🗄️ Data Model

### **Source Data Structure:**
```json
{
    "newsTitle": "Article Title",
    "timestamp": "2025-10-03T10:30:00Z",
    "url_source": "https://example.com/article",
    "content": "Article content...",
    "source": "News Source Name",
    "author": "Author Name",
    "urlToImage": "https://example.com/image.jpg",
    "processed_at": "2025-10-03T10:35:00Z"
}
```

### **Analytical Tables:**

#### **1. Main Data Table: `news_api_data`**
- **Purpose**: Raw news articles with full content
- **Schema**: Auto-inferred from Parquet files
- **Content**: All article fields including title, content, source, author, timestamps

#### **2. News Source Summary: `summary_news`**
- **Purpose**: News source analytics and statistics
- **Metrics**: Article count, date range, source popularity
- **Use Cases**: Source performance analysis, content volume tracking

#### **3. Author Activity: `author_activity`**
- **Purpose**: Author productivity and distribution analysis
- **Metrics**: Article count, latest activity, source diversity
- **Use Cases**: Author performance tracking, content creator analysis

## 🔧 Technical Components

### **1. News Data Extraction (`**fetch_news.py**`)**

**Core Functions:**
- **`get_api_key_from_airflow()`**: Secure API key retrieval from Airflow Variables
- **`fetch_news_from_api()`**: Paginated news fetching with comprehensive coverage
- **`process_articles_to_dataframe()`**: Data cleaning and structure conversion
- **`upload_to_gcs()`**: Cloud storage integration with automatic cleanup

**Key Features:**
- **Pagination Support**: Fetches all available articles (not just first 100)
- **Content Cleaning**: Intelligent content trimming and validation
- **Error Handling**: Comprehensive exception handling and logging
- **Airflow Integration**: Seamless integration with Airflow Variables

### **2. Airflow Orchestration (`news_api_airflow_job.py`)**

**DAG Configuration:**
- **Schedule**: Daily execution
- **Start Date**: October 3, 2025
- **Retry Logic**: Configurable retry attempts
- **Error Handling**: Comprehensive failure management

**Task Pipeline:**

<img width="626" height="60" alt="image" src="https://github.com/user-attachments/assets/04905c77-477e-42d3-b9ed-e02ed0d5fd56" />


 









