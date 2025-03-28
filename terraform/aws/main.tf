provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = var.s3_bucket_name
}

resource "aws_s3_object" "lambda_code" {
  bucket = aws_s3_bucket.lambda_bucket.id
  key    = "lambda_function.zip"
  source = "aws_lambda_function.zip"
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_lambda_function" "quantum_kmeans_lambda" {
  function_name    = "QuantumKMeansLambda-1"
  role            = aws_iam_role.lambda_role.arn
  handler         = "aws_lambda_function.lambda_handler"
  runtime         = "python3.8"
  filename        = aws_s3_object.lambda_code.source
  source_code_hash = filebase64sha256("aws_lambda_function.zip")

  environment {
    variables = {
      S3_BUCKET_NAME = var.s3_bucket_name
    }
  }
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.quantum_kmeans_lambda.function_name
  principal     = "apigateway.amazonaws.com"
}
