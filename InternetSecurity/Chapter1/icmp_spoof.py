#!/usr/bin/python3
from scapy.all import *

print("SENDING SPOOFED ICMP PACKET.......")
ip = IP(src="10.0.2.69", dst="93.184.216.34")
icmp = ICMP()
pkt = ip/icmp
pkt.show()
send(pkt, verbose=0)
