from pwn import *


x = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927')


for i in range(256):

    m = str(xor(x,i),encoding='ISO8859-1')

    if m[6]=='crypto' in m:

        print(i)
        print(m)