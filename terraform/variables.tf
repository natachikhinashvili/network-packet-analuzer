 variable "serviceacc" {
    description = "The path to service account json file."
    default = "file(/home/nata/Downloads/networkpacketanalyzator-b1756629b74a.json)"
}
variable "region" {
    description = "The AWS region to deploy resources."
    default = "us-central1"
}
variable "zone" {
    description = "The AWS zone to deploy resources."
    default = "us-central1-c"
}
variable "projectname" {
    description = "The project name."
    default = "networkpacketanalyzator"
}
variable "location" {
    description = "The AWS location to deploy resources."
    default = "US"
}