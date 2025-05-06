import os
import io
from azure.storage.blob import BlobServiceClient
import pandas as pd

# Azure Blob connection details
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "customer-feedback"
blob_name = "customer_feedback.csv"

# Create BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Download the blob data
blob_client = container_client.get_blob_client(blob_name)
download_stream = blob_client.download_blob()

# Convert the blob data to pandas DataFrame
data = download_stream.readall()
df = pd.read_csv(io.StringIO(data.decode('utf-8')))

print(df)

# Simple data cleaning: removing punctuation and converting to lowercase
df['Feedback'] = df['Feedback'].str.replace(r'[^a-zA-Z\s]', '', regex=True)
df['Feedback'] = df['Feedback'].str.lower()

print(df.head())
