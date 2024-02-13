#!/usr/bin/python3

from scapy.all import *

pkt = Ether()/IP()/ICMP()/"hello"

print(pkt[Raw])
