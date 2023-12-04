import pcapy
import logging
import signal
import sys
import keyboard

from Config import Config
from PycapParser import Parsepycap
from Managedata import ManageData

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%{levelname}s:%(name)s:%(message)s')

file_handler = logging.FileHandler('analyzer_log.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def stop_handler(signum, frame):
    print("signum {}, frame: {}".format(signum, frame))

signal.signal(signal.SIGINT, stop_handler)

def main():
    config = Config()
    config_file = config.get_conf_file()
    interface = config.read_interface(config_file)
    runtimes =  int(config.get_run_times(config_file))
    cap = pcapy.open_live(interface, 65536, 1, 0)
    myfile = ""
    manageData = ManageData()
    notdone=True

    runtimecount = 0
    while notdone:
        header, packet = cap.next()

        unpacked = Parsepycap.unpackheader(packet)
        decoded = Parsepycap.decodeInfo(*unpacked)
        logger.info("Interface {}, Timestamp: {}, Packet Length: {} bytes,\n src mac: {}, dst_mac: {}, arp operation: {},\n src ip: {}, dst ip: {}".format(interface, header["ts"], header["len"], *decoded))
        myfile = manageData.write_to_file("Interface {}, Timestamp: {}, Packet Length: {} bytes ,\n src mac: {}, dst_mac: {}, arp operation: {},\n src ip: {}, dst ip: {} \n".format(interface, header.getts(), header.getlen(), *decoded))
        runtimecount+=1
        if keyboard.is_pressed('s'):
            raise KeyboardInterrupt
    manageData.upload_to_gcs(myfile)

if __name__ == '__main__':
    main()