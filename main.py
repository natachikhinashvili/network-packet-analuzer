import pcapy

from getconfile import Getconfile

from SetInterface import SetInterface
from PycapParser import Parsepycap

from Managedata import ManageData


def main():
        interface = SetInterface.read_interface(Getconfile.get_conffile())
        runtimes =  int(Getconfile.getruntimes(Getconfile.get_conffile()))
        cap = pcapy.open_live(interface, 65536, 1, 0)
        myfile = ""
        runtimecount = 0
        while runtimecount < runtimes:

            header, packet = cap.next()

            unpacked = Parsepycap.unpackheader(packet)
            decoded = Parsepycap.decodeInfo(*unpacked)
            myfile = ManageData.write_to_file("Interface {}, Timestamp: {}, Packet Length: {} bytes ,\n src mac: {}, dst_mac: {}, arp operation: {},\n src ip: {}, dst ip: {} \n".format(interface, header.getts(), header.getlen(), *decoded))
            runtimecount+=1
        ManageData.upload_to_gcs(myfile)

if __name__ == '__main__':
    main()