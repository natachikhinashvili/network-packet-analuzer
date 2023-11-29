import pcapy

from Config import Config
from PycapParser import Parsepycap
from Managedata import ManageData


def main():
    config = Config()
    config_file = config.get_conf_file()
    interface = config.read_interface(config_file)
    runtimes =  int(config.get_run_times(config_file))
    cap = pcapy.open_live(interface, 65536, 1, 0)
    myfile = ""
    manageData = ManageData()

    runtimecount = 0
    while runtimecount < runtimes:

        header, packet = cap.next()

        unpacked = Parsepycap.unpackheader(packet)
        decoded = Parsepycap.decodeInfo(*unpacked)
        myfile = manageData.write_to_file("Interface {}, Timestamp: {}, Packet Length: {} bytes ,\n src mac: {}, dst_mac: {}, arp operation: {},\n src ip: {}, dst ip: {} \n".format(interface, header.getts(), header.getlen(), *decoded))
        runtimecount+=1
    manageData.upload_to_gcs(myfile)

if __name__ == '__main__':
    main()