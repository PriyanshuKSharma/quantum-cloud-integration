from google.cloud import storage
import os

GCP_STORAGE_BUCKET = os.getenv("GCP_STORAGE_BUCKET", "quantum-kmeans-gcp")

storage_client = storage.Client()

def upload_to_gcp(file_path, blob_name):
    """Uploads a file to Google Cloud Storage."""
    bucket = storage_client.bucket(GCP_STORAGE_BUCKET)
    blob = bucket.blob(blob_name)
    try:
        blob.upload_from_filename(file_path)
        print(f"File {file_path} uploaded to {GCP_STORAGE_BUCKET}/{blob_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_from_gcp(blob_name, dest_path):
    """Downloads a file from Google Cloud Storage."""
    bucket = storage_client.bucket(GCP_STORAGE_BUCKET)
    blob = bucket.blob(blob_name)
    try:
        blob.download_to_filename(dest_path)
        print(f"File {blob_name} downloaded to {dest_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")
