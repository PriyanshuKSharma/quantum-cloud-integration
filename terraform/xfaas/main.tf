# XFaaS Infrastructure as Code
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

provider "azurerm" {
  features {}
}

provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

# AWS Lambda Function
resource "aws_lambda_function" "quantum_processor_aws" {
  filename         = "aws_lambda_deployment.zip"
  function_name    = "quantum-processor-aws"
  role            = aws_iam_role.lambda_role.arn
  handler         = "aws_lambda_handler.lambda_handler"
  runtime         = "python3.9"
  timeout         = 300
  memory_size     = 1024
}

resource "aws_iam_role" "lambda_role" {
  name = "quantum-lambda-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# Azure Function App
resource "azurerm_resource_group" "quantum_rg" {
  name     = "quantum-xfaas-rg"
  location = var.azure_location
}

resource "azurerm_linux_function_app" "quantum_function_azure" {
  name                = "quantum-processor-azure"
  resource_group_name = azurerm_resource_group.quantum_rg.name
  location           = azurerm_resource_group.quantum_rg.location
  
  storage_account_name = azurerm_storage_account.quantum_storage.name
  service_plan_id     = azurerm_service_plan.quantum_plan.id

  site_config {
    application_stack {
      python_version = "3.9"
    }
  }
}

# Google Cloud Function
resource "google_cloudfunctions_function" "quantum_processor_gcp" {
  name        = "quantum-processor-gcp"
  runtime     = "python39"
  available_memory_mb = 1024
  source_archive_bucket = google_storage_bucket.function_bucket.name
  source_archive_object = "function-source.zip"
  trigger {
    http_trigger {}
  }
  entry_point = "quantum_processor"
}