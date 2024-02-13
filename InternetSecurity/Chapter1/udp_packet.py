#!/bin/env python3
import socket

data = b"Hello World\n"
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.sendto(data, ("0.0.0.0", 9090))
