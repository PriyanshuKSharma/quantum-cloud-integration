variable "s3_bucket_name" {
  description = "S3 bucket for storing input/output data"
  type        = string
  default     = "quantum-kmeans-bucket-research-terraform"
}
variable "function_name" {
  description = "Name of the AWS Lambda function"
  type        = string
  default     = "quantum-kmeans-lambda-research-terraform"
}