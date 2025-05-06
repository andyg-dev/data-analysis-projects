CREATE OR REPLACE DATABASE customer_feedback_db;
USE DATABASE customer_feedback_db;
CREATE OR REPLACE SCHEMA feedback_schema;
USE SCHEMA feedback_schema;

CREATE OR REPLACE TABLE customer_feedback (
    CustomerID STRING,
    Feedback STRING,
    Timestamp TIMESTAMP,
    AgentID STRING,
    Sentiment STRING
);

SHOW DATABASES;

CREATE OR REPLACE STAGE feedback_stage;

COPY INTO customer_feedback
FROM @feedback_stage/feedback_with_sentiment.csv
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER = 1);

SELECT * FROM customer_feedback;

CREATE OR REPLACE VIEW agent_sentiment_summary AS
SELECT 
    AgentID,
    COUNT(*) AS Total_Feedbacks,
    COUNT(CASE WHEN Sentiment = 'positive' THEN 1 END) AS Positive_Count,
    COUNT(CASE WHEN Sentiment = 'negative' THEN 1 END) AS Negative_Count,
    COUNT(CASE WHEN Sentiment = 'neutral' THEN 1 END) AS Neutral_Count
FROM customer_feedback
GROUP BY AgentID;

SELECT * FROM agent_sentiment_summary;

