import argparse
import configparser

config = configparser.ConfigParser()

class Config:
    def get_conf_file(self):
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument('config_file')

            args = parser.parse_args()

            return args.config_file
        except FileNotFoundError:
            print('File not implemented')

    def read_interface(self, conf_file):
        try:
            config.read(conf_file)
            sections = config.sections()
            return config[sections[0]][sections[0]]
        except NotImplementedError:
            print("Interface field is not implemented in conf file")
    
    def get_log_file(self, conf_file):
        try:
            config.read(conf_file)
            sections = config.sections()
            return config[sections[1]][sections[1]]
        except NotImplementedError:
            print("logfile field is not implemented in conf file")
        
    def get_run_times(self, conf_file):
        try:
            config.read(conf_file)
            sections = config.sections()
            return config[sections[2]][sections[2]]
        except NotImplementedError:
            print("runtimes field is not implemented in conf file")