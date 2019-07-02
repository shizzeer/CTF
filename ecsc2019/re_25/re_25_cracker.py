from z3 import *
import string
import random

alphabet = string.printable

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

def verify(first_char, second_char, third_char, esi, edx):#first_char, second_char, third_char, esi, edx):
	eax = (esi + 3) & 0xFFFFFFFF
	esi &= esi
	r9 = edx & 0xFFFFFFFF
	eax = esi & 0xFFFFFFFF
	eax >>= 2
	edx = eax * 4
	r10 = eax & 0xFFFFFFFF
	r10 *= -1
	eax &= eax
	eax = esi & 0xFFFFFFFF
	eax &= 3
	if (eax & 0xFFFFFFFF) != 2:
		if (eax & 0xFFFFFFFF == 3):
			edx = third_char & 0xFF
			edx = (edx << 16) & 0xFFFFFFFF
			eax = second_char & 0xFF
			eax = (eax << 8) & 0xFFFFFFFF
			edx = (edx ^ eax) & 0xFFFFFFFF
			eax = first_char & 0xFF
			eax = (eax ^ edx) & 0xFFFFFFFF
			eax = (eax * 0xCC9E2D51) & 0xFFFFFFFF
			eax = rol(eax, 0xf, 32) & 0xFFFFFFFF
			eax = (eax * 0x1B873593) & 0xFFFFFFFF
			r9 = (r9 ^ eax) & 0xFFFFFFFF
			esi = (esi ^ r9) & 0xFFFFFFFF
			eax = esi & 0xFFFFFFFF
			edx = esi & 0xFFFFFFFF
			eax = (eax >> 0x10) & 0xFFFFFFFF
			edx = (edx ^ eax) & 0xFFFFFFFF
			eax = (edx * 0x85EBCA6B) & 0xFFFFFFFF
			r9 = eax & 0xFFFFFFFF
			r9 = (r9 >> 0x0d) & 0xFFFFFFFF
			eax = (eax ^ r9) & 0xFFFFFFFF
			eax = (eax * 0xC2B2AE35) & 0xFFFFFFFF
			edx = eax & 0xFFFFFFFF
			edx = (edx >> 0x10) & 0xFFFFFFFF
			eax = (eax ^ edx) & 0xFFFFFFFF
			print hex(eax)
			return eax == 0x49A30836

#s = Solver()
#first_char = BitVec('first_char', 8)
#second_char = BitVec('second_char', 8)
#third_char = BitVec('third_char', 8)

#s.add(verify(first_char, second_char, third_char, 3, 1337) == True)
#if s.check() == sat:
#       print s.model()

a = ord(random.choice(alphabet))
b = ord(random.choice(alphabet))
c = ord(random.choice(alphabet))

while True:
	if verify(a, b, c, 3, 1337) == True:
		print a
		print b
		print c
		break
	a = ord(random.choice(alphabet))
	b = ord(random.choice(alphabet))
	c = ord(random.choice(alphabet))
