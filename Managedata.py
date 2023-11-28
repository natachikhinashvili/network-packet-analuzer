import os
import re

from google.cloud import storage

from dataclasses import dataclass
from FilterByArp import FilterByArp
from getconfile import Getconfile

outputfile = "output"
max_lines = 10000
file_counter = 0
line_count = 0
filename=""

if Getconfile.getlogfile(Getconfile.get_conffile()):
    filename = Getconfile.getlogfile(Getconfile.get_conffile())
else:
    filename = f"{outputfile}_{file_counter}.txt"


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/nata/Downloads/networkpacketanalyzator-b1756629b74a.json"


@dataclass
class ManageData:
    def upload_to_gcs(filename):
        client = storage.Client()
        bucket_name = "netwrok_packets"
        bucket = client.get_bucket(bucket_name)

        with open(filename, "rb") as data:
            blob = bucket.blob(filename)
            blob.upload_from_file(data)

    def write_to_file(line):
        global file_counter
        global line_count
        global filename

        if line_count == 0 or line_count % max_lines == 0:
            file_counter += 1
            if Getconfile.getlogfile(Getconfile.get_conffile()):
                original= Getconfile.getlogfile(Getconfile.get_conffile())
                sanitizedname=re.sub(r'[^\w.-]', '_', original)
                filename = f"{sanitizedname}_{file_counter}.txt"
            else:
                filename = f"{outputfile}_{file_counter}.txt"
            with open(filename, "w") as file:
                file.write(line)
        else:
            with open(filename, "a") as file:
                file.write(line)

        line_count+=1
        return filename