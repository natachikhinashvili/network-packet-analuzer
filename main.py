import pcapy
import signal
import keyboard

from Config import Config
from PycapParser import Parsepycap
from Managedata import ManageData
from loggerhandlers import logger
from signalhandler import stop_handler

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
        signal.signal(signal.SIGINT, stop_handler, notdone)
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