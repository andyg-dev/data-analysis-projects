# Azure + Snowflake ETL & Sentiment Analysis Pipeline
This project demonstrates a full end-to-end data pipeline using Python, Azure, and Snowflake, focusing on extracting customer feedback and applying AI-powered sentiment analysis to drive insights into agent performance.

## Pipeline Diagram

![Pipeline Diagram](https://github.com/andyg-dev/data-analysis-projects/blob/main/azure_ai_snowflake_speech_analytics/pipeline_diagram.jpg?raw=true)

## Pipeline Overview
Data Extraction & Cleaning:

- Structured customer feedback data is extracted from various sources.

- A Python script cleans and preprocesses this data.

- The cleaned data is uploaded to Azure Blob Storage.

Sentiment Analysis:

- Azure AI Language service analyzes the sentiment of the feedback (positive, negative, neutral).

- Data Loading into Snowflake:

- The processed data is staged in Azure Blob Storage.

- Using Azure Data Factory, data is loaded into Snowflake.

- A Snowflake view is created to summarize agent sentiment performance metrics.

## 🛠️ Technologies
Azure Blob Storage for cloud data storage

Azure AI Language for sentiment analysis

Snowflake for data warehousing and analytics

Python (Pandas) for scripting and uploading to Azure Blob Storage

SQL for database/table/view creation and reporting

![Sentiment Analysis Results](https://github.com/andyg-dev/data-analysis-projects/blob/main/azure_ai_snowflake_speech_analytics/snowflake_sql_sentiment_analysis_results.jpg?raw=true)
