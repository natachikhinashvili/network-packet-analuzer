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