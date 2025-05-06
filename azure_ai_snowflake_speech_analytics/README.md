# Azure + Snowflake ETL & Sentiment Analysis Pipeline
This project demonstrates a full end-to-end data pipeline using Python, Azure, and Snowflake, focusing on extracting customer feedback and applying AI-powered sentiment analysis to drive insights into agent performance.

## 🔧 Features
Extracts structured customer feedback data and cleans it using Python.

Performs sentiment analysis using Azure AI Language service.

Uploads processed data to Azure Blob Storage and loads it into Snowflake via a staging area.

Creates a Snowflake view to summarize agent sentiment performance metrics (positive/negative/neutral).

## 🛠️ Technologies
Azure Blob Storage for cloud data storage

Azure AI Language for sentiment analysis

Snowflake for data warehousing and analytics

Python (Pandas) for scripting and uploading to Azure Blob Storage

SQL for database/table/view creation and reporting

![Sentiment Analysis Results](https://github.com/andyg-dev/data-analysis-projects/blob/main/azure_ai_snowflake_speech_analytics/snowflake_sql_sentiment_analysis_results.jpg?raw=true)
