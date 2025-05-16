# Azure, Snowflake, SQL Server ETL & AI Sentiment Analysis Pipeline
This project demonstrates a strong understanding of **full end-to-end data pipeline**. Using Python (pandas), Azure Blob Storage, Azure SQL database, Azure Data Studio, Azure Co-Pilot, Azure AI Text Analytics and Snowflake, this project analyzes customer feedback and bins negative, neutral, positive feedback. This prcoess helps **tech startups** with insights into **customer service rep performance**.

## Pipeline Diagram

![Pipeline Diagram](https://github.com/andyg-dev/data-analysis-projects/blob/main/azure_ai_snowflake_speech_analytics/pipeline_diagram.jpg?raw=true)

## Pipeline Overview
Data Extraction & Cleaning:

- Structured customer feedback data is extracted from various sources.

- A Python script cleans and preprocesses this data.

- The cleaned data is uploaded to Azure Blob Storage and Azure SQL Server through Data Studio.

Sentiment Analysis:

- Azure AI Language service analyzes the sentiment of the feedback (positive, negative, neutral).

- Data Loading into Snowflake.

- The processed data is staged in Azure Blob Storage.

- Integrate Snowflake with Azure Blob Storage to load data into Snowflake

- A Snowflake view is created to summarize agent sentiment performance metrics.

## 🛠️ Technologies
- Azure Blob Storage for cloud data storage

- Azure SQL Server for relational databases
- 
- Azure AI Language for sentiment analysis

- Snowflake for data warehousing and analytics

- Azure Data Studio for database/table/view creation and reporting

- Azure Co-Pilot for queries and project management

- Python (Pandas) for scripting and uploading to Azure Blob Storage

![Sentiment Analysis Results](https://github.com/andyg-dev/data-analysis-projects/blob/main/azure_ai_snowflake_speech_analytics/snowflake_sql_sentiment_analysis_results.jpg?raw=true)
