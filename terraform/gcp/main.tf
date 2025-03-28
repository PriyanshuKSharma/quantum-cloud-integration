provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

resource "google_storage_bucket" "quantum_kmeans_bucket" {
  name     = "quantum-kmeans-gcp"
  location = var.gcp_region
}

resource "google_storage_bucket_object" "function_code" {
  name   = "gcp_function.zip"
  bucket = google_storage_bucket.quantum_kmeans_bucket.name
  source = "gcp_function.zip"
}

resource "google_cloudfunctions2_function" "quantum_kmeans" {
  name        = "quantum-kmeans-gcp"
  location    = var.gcp_region
  description = "GCP function for Quantum K-Means"

  build_config {
    runtime     = "python310"
    entry_point = "process_data"

    source {
      storage_source {
        bucket = google_storage_bucket.quantum_kmeans_bucket.name
        object = google_storage_bucket_object.function_code.name
      }
    }
  }

  service_config {
    min_instance_count = 0
    max_instance_count = 1
  }
}
