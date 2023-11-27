from dataclasses import dataclass
@dataclass
class DecodeInfo:
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