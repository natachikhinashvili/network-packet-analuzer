import argparse
from dataclasses import dataclass

@dataclass
class GetInterface:
    def get_interface():
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument('config_file')

            args = parser.parse_args()

            return args.config_file
        except FileNotFoundError:
            print('File not implemented')

    def read_interface(conf_file):
        try:
            with open(conf_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if 'interface=' in line:
                        return line.split('=')[1]
        except NotImplementedError:
            print("Interface field is not implemented in conf file")