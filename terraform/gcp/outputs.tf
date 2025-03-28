output "gcp_function_url" {
  value = google_cloudfunctions2_function.quantum_kmeans.url
}
output "gcp_storage_bucket" {
  value = google_storage_bucket.quantum_kmeans_bucket.name
}
