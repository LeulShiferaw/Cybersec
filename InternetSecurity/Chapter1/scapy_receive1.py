#!/usr/bin/python3

from scapy.all import *

ip = IP(dst="100.0.0.1")
udp = UDP()
pkt = ip/udp
reply = sr1(pkt)
print("ICMP reply .........")
print("Source IP: ", reply[IP].src)
print("Destination IP: ", reply[IP].dst)
