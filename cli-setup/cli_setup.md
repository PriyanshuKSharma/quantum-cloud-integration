# Cloud CLI Setup Guide

This guide provides step-by-step instructions to set up and configure AWS CLI, Azure CLI, and GCP CLI.

## AWS CLI Setup

1. **Download AWS CLI**: [AWS CLI v2](https://awscli.amazonaws.com/AWSCLIV2.msi)
2. **Install AWS CLI and verify installation:**
   ```sh
   aws --version
   ```
3. **Configure AWS CLI:**
   ```sh
   aws configure
   ```
   Enter the following details:
   - **AWS Access Key**
   - **AWS Secret Access Key**
   - **Default region** (e.g., `us-east-1`)
   - **Output format** (e.g., `json`)
4. **Verify configuration:**
   ```sh
   aws s3 ls
   ```

## Azure CLI Setup

1. **Download Azure CLI**: [Azure CLI](https://aka.ms/installazurecliwindows)
2. **Install and verify installation:**
   ```sh
   az --version
   ```
3. **Login to Azure:**
   ```sh
   az login
   ```
4. **Set default subscription:**
   ```sh
   az account set --subscription "SUBSCRIPTION_ID"
   ```
5. **Verify Azure Storage accounts:**
   ```sh
   az storage account list
   ```

## GCP CLI Setup

1. **Download Google Cloud SDK**: [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
2. **Install and verify installation:**
   ```sh
   gcloud version
   ```
3. **Authenticate with Google Cloud:**
   ```sh
   gcloud auth login
   ```
4. **Set default project:**
   ```sh
   gcloud config set project PROJECT_ID
   ```
5. **Verify Cloud Storage buckets:**
   ```sh
   gcloud storage buckets list
   ```


