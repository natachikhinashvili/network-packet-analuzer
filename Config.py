import argparse
import configparser

config = configparser.ConfigParser()

class Config:
    def __init__(self, conf_file):
        config.read(conf_file)
        sections = config.sections()
        
    def get_conf_file(self):
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument('config_file')

            args = parser.parse_args()

            return args.config_file
        except FileNotFoundError:
            print('File not implemented')

    def read_interface(self):
        try:
            return config[self.sections['interface']][self.sections['interface']]
        except NotImplementedError:
            print("Interface field is not implemented in conf file")
    
    def get_log_file(self):
        try:
            return config[self.sections['logging']][self.sections['logging']]
        except NotImplementedError:
            print("logfile field is not implemented in conf file")
        
    def get_run_times(self):
        try:
            return config[self.sections['runtimes']][self.sections['runtimes']]
        except NotImplementedError:
            print("runtimes field is not implemented in conf file")