#!/usr/bin/python3

from scapy.all import *

ip = IP(ttl=100, src="1.2.3.4", dst="10.2.5.10")
icmp = ICMP()
pkt = ip/icmp
send(pkt, verbose=0)
