from azure.storage.blob import BlobServiceClient
import os

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "quantumdata")

blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

def upload_to_azure(file_path, blob_name):
    """Uploads a file to Azure Blob Storage."""
    blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=blob_name)
    try:
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"File {file_path} uploaded to {blob_name} in Azure Blob Storage")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_from_azure(blob_name, dest_path):
    """Downloads a file from Azure Blob Storage."""
    blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=blob_name)
    try:
        with open(dest_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        print(f"File {blob_name} downloaded to {dest_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")
