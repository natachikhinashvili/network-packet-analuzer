from google.cloud import storage
import os
from dataclasses import dataclass

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/nata/Downloads/networkpacketanalyzator-b1756629b74a.json"

@dataclass
class Upload_to_gcs:
    def upload_to_gcs(filename):
        client = storage.Client()
        bucket_name = "netwrok_packets"
        bucket = client.get_bucket(bucket_name)

        with open(filename, "rb") as data:
            blob = bucket.blob(filename)
            blob.upload_from_file(data)