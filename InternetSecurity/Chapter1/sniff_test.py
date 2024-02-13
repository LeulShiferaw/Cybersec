#!/usr/bin/python3
from scapy.all import *

def print_pkt(pkt):
    print(pkt.summary())

pkt = sniff(iface='enp0s3', filter='tcp', prn=print_pkt)
