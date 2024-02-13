#!/usr/bin/python3

from scapy.all import *

def print_pkt(pkt):
    print(pkt.summary())

pkt = sniff(iface='enp0s3', filter='udp and dst host 8.8.8.8 and dst port 53', prn=print_pkt)
