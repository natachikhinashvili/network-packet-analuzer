import pcapy

from UnpackHeader import UnpackHeader
from getconfile import Getconfile
from DecodeInfo import DecodeInfo

from upload_to_gcs import Upload_to_gcs
from write_to_file import Write_to_file
from SetInterface import SetInterface


def main():
        
        cap = pcapy.open_live(SetInterface.read_interface(Getconfile.get_conffile()), 65536, 1, 0)
        while True:

            header, packet = cap.next()

            unpacked = UnpackHeader.unpackheader(packet)
            decoded = DecodeInfo.decodeInfo(*unpacked)
            myfile = Write_to_file.write_to_file("Interface {}, Timestamp: {}, Packet Length: {} bytes ,\n src mac: {}, dst_mac: {}, arp operation: {},\n src ip: {}, dst ip: {} \n".format(interface, header.getts(), header.getlen(), *decoded))
            Upload_to_gcs.upload_to_gcs(myfile)

if __name__ == '__main__':
    main()