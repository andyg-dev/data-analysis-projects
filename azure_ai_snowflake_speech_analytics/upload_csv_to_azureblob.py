from azure.storage.blob import BlobServiceClient
import os

# Set up connection to Azure Blob Storage
connection_string = "DefaultEndpointsProtocol=https;AccountName=andybiportal;AccountKey=UMUiEcrtsdVGSRUlozTb/RUu8Eayb74g+ZS3nzNNFhBRf3n4/B9nzUjsew4W89x0vptQqZA/cCFE+ASt4pHZKw==;EndpointSuffix=core.windows.net"
container_name = "customer-feedback"  # Replace with your container name
blob_name = "customer_feedback.csv"  # Name to give the uploaded file
file_path = "customer_feedback.csv"  # Path to your local CSV

# Create BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# Upload the CSV to Azure Blob Storage
with open(file_path, "rb") as data:
    container_client.upload_blob(blob_name, data, overwrite=True)

print(f"CSV file uploaded to Azure Blob Storage: {container_name}/{blob_name}")
