#!/usr/bin/python3
from scapy.all import *

print("SENDING SPOOFED UDP PACKET.....")
ip = IP(src="10.0.2.13", dst="8.8.8.8")
udp = UDP(sport = 8888, dport=53)
data = "Hello UDP!\n"
pkt = ip/udp/data
pkt.show()
send(pkt, verbose=0)
