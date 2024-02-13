#!/usr/bin/python3
from scapy.all import *

def spoof_icmp(pkt):
    if ICMP in pkt and pkt[ICMP].type == 8:
        print("Received ICMP Echo Request")
        spoofed_pkt = IP(src=pkt[IP].dst, dst=pkt[IP].src)/ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)/pkt[Raw].load
        send(spoofed_pkt, verbose=False)
        print("Spoofed ICMP Echo Reply sent")

# Sniff packets and apply the spoofing function
sniff(filter="icmp", prn=spoof_icmp, store=0)
