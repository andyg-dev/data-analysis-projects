# main.py
import subprocess

def run_pipeline():
    # Step 1: Extract data and save to CSV
    subprocess.run(['python', 'create_csv.py'])

    # Step 2: Transform the data
    subprocess.run(['python', 'extract_transform_data.py'])

    # Step 3: Upload the transformed CSV to Azure Blob Storage
    subprocess.run(['python', 'upload_csv_to_azureblob.py'])

    # Step 4: Perform Sentiment Analysis on the transformed data
    subprocess.run(['python', 'sentiment_analysis_azure_ai_language.py'])

if __name__ == '__main__':
    run_pipeline()
