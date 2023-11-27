provider "google" {
  credentials = var.serviceacc
  project = var.projectname
  region = var.region
  zone = var.zone
}

resource "google_storage_bucket" "static-site" {
  name= "network_packet_analyzator"
  location= var.location
  storage_class = "STANDARD"
}

resource "google_project_iam_binding" "project_binding" {
  project = var.projectname
  role    = "roles/storage.admin"

  members = [
    "serviceAccount:${var.serviceacc}",
  ]
}
resource "google_service_account" "my_service_account" {
  account_id   = var.serviceacc
  display_name = "My Service Account"
  project      = var.projectname
}

resource "google_service_account_key" "my_key" {
  service_account_id = google_service_account.my_service_account.account_id
  private_key_type   = "json"
}