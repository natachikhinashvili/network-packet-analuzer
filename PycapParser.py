from struct import unpack
from dataclasses import dataclass

@dataclass
class Parsepycap:
    def unpackheader(packet):
            eth_header = unpack('!6s6sH', packet[:14])
            arp_header = unpack('2s2s1s1s2s6s4s6s4s', packet[14:42])
            return eth_header, arp_header

    def decodeInfo(eth_header, arp_header):
            src_mac = ""
            dst_mac = ""
            arp_operation=""
            for b in eth_header[0]:
                src_mac = ':'.join(f'{b:02x}' )
            for b in eth_header[1]:
                dst_mac = ':'.join(f'{b:02x}')
            if int.from_bytes(arp_header[4], byteorder='big') == 1:
                arp_operation = 'Request'
            elif int.from_bytes(arp_header[4], byteorder='big') == 2:
                arp_operation = 'Reply'
            src_ip = '.'.join(map(str, arp_header[5]))
            dst_ip = '.'.join(map(str, arp_header[7]))
            return src_mac, dst_mac, arp_operation, src_ip, dst_ip