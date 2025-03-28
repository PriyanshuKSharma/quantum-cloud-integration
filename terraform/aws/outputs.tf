output "aws_lambda_function_name" {
  value = aws_lambda_function.quantum_kmeans_lambda.function_name
}
output "s3_bucket" {
  value = aws_s3_bucket.lambda_bucket.bucket
}
