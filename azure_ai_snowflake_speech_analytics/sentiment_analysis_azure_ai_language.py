import os
import pandas as pd
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Retrieve API credentials from environment variables
endpoint = os.getenv("AZURE_TEXT_ANALYTICS_ENDPOINT")
subscription_key = os.getenv("AZURE_TEXT_ANALYTICS_KEY")

# Ensure credentials are valid
if not endpoint or not subscription_key:
    raise ValueError("Azure Text Analytics credentials are missing. Check environment variables.")

# Initialize the Text Analytics client
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(subscription_key))

# Perform sentiment analysis
def analyze_sentiment(feedback_text):
    # Ensure the feedback is not empty or None
    if not feedback_text:
        return "No Feedback" 

    documents = [feedback_text]
    try:
        response = client.analyze_sentiment(documents=documents)
        # Extract sentiment value (Positive, Negative, Neutral, Mixed)
        return response[0].sentiment
    except Exception as e:
        print(f"Error analyzing sentiment for text: {feedback_text}. Error: {e}")
        return "Error" 

# Load the transformed CSV file 
df = pd.read_csv('customer_feedback.csv')

# Apply sentiment analysis to the feedback data
df['Sentiment'] = df['Feedback'].apply(analyze_sentiment)

# Print the DataFrame with sentiment results
print(df)

# Optionally, save the results to a new CSV file
df.to_csv('feedback_with_sentiment.csv', index=False)
