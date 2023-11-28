import argparse
from dataclasses import dataclass

@dataclass
class Getconfile:
    def get_conffile():
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument('config_file')

            args = parser.parse_args()

            return args.config_file
        except FileNotFoundError:
            print('File not implemented')

    
    def getlogfile(conf_file):
        try:
            with open(conf_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if 'logfile=' in line:
                        return line.split('=')[1]
        except NotImplementedError:
            print("logfile field is not implemented in conf file")
        
    def getruntimes(conf_file):
        try:
            with open(conf_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if 'runtimes=' in line:
                        return line.split('=')[1]
        except NotImplementedError:
            print("runtimes field is not implemented in conf file")