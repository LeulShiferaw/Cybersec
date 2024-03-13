#!/usr/bin/python3
from scapy.all import *
import time

ID = 1000
dst_ip = "10.9.0.5"

#Frag No. 1
ip = IP(dst=dst_ip, id=ID, frag=0, flags=1)
udp = UDP(sport=7070, dport=9090, chksum=0)
udp.len = 8 + 32 + 40 + 20
payload = "A"*31 + "\n"
pkt1 = ip/udp/payload

#Frag No. 2
ip = IP(dst=dst_ip, id=ID, frag=5, flags=1)
ip.proto = 17
payload = "B" * 39 + "\n"
pkt2 = ip/payload

#Frag No. 3
ip = IP(dst=dst_ip, id=ID, frag=10, flags=0)
ip.proto = 17
payload = "C" * 19 + "\n"
pkt3 = ip/payload

send(pkt1)
send(pkt3)
time.sleep(5)
send(pkt2)
