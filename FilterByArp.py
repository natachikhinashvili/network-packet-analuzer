from dataclasses import dataclass

@dataclass
class FilterByArp:
    def filterbyarp(arp_method, mydata):
        methods = []
        for line in mydata:
            if f"arp operation: {arp_method}" in line:
                methods.append(mydata[mydata.index(line) - 1])
                methods.append(line)
                methods.append(mydata[mydata.index(line) + 1])
        return methods