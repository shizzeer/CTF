from z3 import *
from pwn import *

key = [Int('x{}'.format(i)) for i in range(16)]	# a list of the variables to solve

s = Solver()
for i in range(16):
	s.add(key[i] >= 0, key[i] <= 35)	# constraints to "say" the solver that our variables has to be in the range from 0 to
	# 35

# key_constraints from disassembled file
s.add((key[0] + key[1]) % 0x24 == 0xe)
s.add((key[2] + key[3]) % 0x24 == 0x18)
s.add((key[2] - key[0]) % 0x24 == 6)
s.add((key[1] + key[3] + key[5]) % 0x24 == 4)
s.add((key[2] + key[4] + key[6]) % 0x24 == 0xd)
s.add((key[3] + key[4] + key[5]) % 0x24 == 0x16)
s.add((key[6] + key[8] + key[10]) % 0x24 == 0x1f)
s.add((key[1] + key[4] + key[7]) % 0x24 == 7)
s.add((key[9] + key[12] + key[15]) % 0x24 == 0x14)
s.add((key[13] + key[14] + key[15]) % 0x24 == 0xc)
s.add((key[8] + key[9] + key[10]) % 0x24 == 0x1b)
s.add((key[7] + key[12] + key[13]) % 0x24 == 0x17)

correct_key = []

# If the problem is satisfiable then we can assembled correct key
if s.check() == sat:
	m = s.model()
	for i in range(16):
		if m[key[i]].as_long() >= ord('A') - 0x37:
			correct_key.append(chr(m[key[i]].as_long() + 0x37))
		else:
			correct_key.append(chr(m[key[i]].as_long() + 0x30))
	print 'KEY: ' + ''.join(correct_key)

session = ssh(host='2018shell4.picoctf.com', user='shizzer', password='XXXXXXXXXXXXXX')
shell = session.run('sh')
shell.sendline('cd /problems/keygen-me-2_1_762036cde49fef79146a706d0eda80a3; ./activate ' + ''.join(correct_key))
print shell.recvline()
