provider "aws" {
  region = "us-east-1"
}

# variable "s3_bucket_name" {
#   default = "quantum-kmeans-bucket-research-terraform"
# }

# Create ZIP automatically
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "lambda_function.py"
  output_path = "aws_lambda_function.zip"
}

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = var.s3_bucket_name
}

resource "aws_s3_object" "lambda_code" {
  bucket = aws_s3_bucket.lambda_bucket.id
  key    = "lambda_function.zip"
  source = data.archive_file.lambda_zip.output_path
  etag   = filemd5(data.archive_file.lambda_zip.output_path)
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

# Attach AWS Lambda Execution Policy
resource "aws_iam_role_policy_attachment" "lambda_execution_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Use S3-based deployment
resource "aws_lambda_function" "quantum_kmeans_lambda" {
  function_name = "QuantumKMeansLambda-1"
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"

  s3_bucket        = aws_s3_bucket.lambda_bucket.id
  s3_key           = aws_s3_object.lambda_code.key
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

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
