#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='br-d1b667a0f3eb', filter='icmp', prn=print_pkt)
