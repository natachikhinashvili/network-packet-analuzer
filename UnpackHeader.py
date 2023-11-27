from struct import unpack
from dataclasses import dataclass
@dataclass
class UnpackHeader():
    def unpackheader(packet):
            eth_header = unpack('!6s6sH', packet[:14])
            arp_header = unpack('2s2s1s1s2s6s4s6s4s', packet[14:42])
            return eth_header, arp_header