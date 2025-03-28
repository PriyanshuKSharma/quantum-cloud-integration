import boto3
import os

AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET", "quantum-kmeans-bucket")

def upload_to_s3(file_path, object_name):
    """Uploads a file to AWS S3."""
    s3_client = boto3.client("s3")
    try:
        s3_client.upload_file(file_path, AWS_S3_BUCKET, object_name)
        print(f"File {file_path} uploaded to {AWS_S3_BUCKET}/{object_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_from_s3(object_name, dest_path):
    """Downloads a file from AWS S3."""
    s3_client = boto3.client("s3")
    try:
        s3_client.download_file(AWS_S3_BUCKET, object_name, dest_path)
        print(f"File {object_name} downloaded to {dest_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")
