import os

from google.cloud import storage

from Config import Config

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/nata/Downloads/networkpacketanalyzator-b1756629b74a.json"

class ManageData:
    max_lines = 10000
    file_counter = 0
    line_count = 0
    filename="output"
    config = Config()
    config_file = config.get_conf_file()


    def upload_to_gcs(filename):

        client = storage.Client()
        bucket_name = "netwrok_packets"
        bucket = client.get_bucket(bucket_name)

        with open(filename, "rb") as data:
            blob = bucket.blob(filename)
            blob.upload_from_file(data)


    def write_to_file(self, line):
        try:
            filename=self.config.get_log_file(self.config_file)
        except FileNotFoundError:
            print("file not implemented")


        if self.line_count == 0 or self.line_count % self.max_lines == 0:

            self.file_counter += 1
            filename = f"{filename}_{self.file_counter}.txt"
            with open(filename, "w") as file:
                file.write(line)

        else:

            with open(filename, "a") as file:
                file.write(line)

        self.line_count+=1
        return filename