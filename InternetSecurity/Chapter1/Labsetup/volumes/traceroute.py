#!/usr/bin/env python3

from scapy.all import *

def traceroute(destination):
    ttl = 1

    while True:
        packet = IP(dst=destination, ttl=ttl) / ICMP()

        reply = sr1(packet, verbose=False, timeout=1)

        if reply is None:
            print(f"{ttl}. *")
        elif reply.type == 0:
            print(f"{ttl}. {reply.src} (Destination reached)")
            break;
        else:
            print(f"{ttl}. {reply.src}")
        ttl += 1

traceroute(str(input("Destination: ")))
