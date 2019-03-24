import string

encrypted_flag = [0x11, 0x80, 0x20, 0xE0, 0x22, 0x53, 0x72, 0xa1, 0x01, 0x41, 0x55, 0x20, 0xa0, 0xc0, 0x25, 
				  0xe3, 0x20, 0x30, 0x00, 0x45, 0x05, 0x35, 0x40, 0x65, 0xc1]

alphabet = string.printable
flag = []

def ror4(encrypted_char):
	encrypted_char_bin = "{0:08b}".format(encrypted_char)
	carry_bits = encrypted_char_bin[-4:]
	encrypted_char_shift = list("{0:08b}".format(encrypted_char >> 4%8))
	
	for i in range(len(carry_bits)):
		encrypted_char_shift[i] = carry_bits[i]

	encrypted_char_shift = int(''.join(encrypted_char_shift), 2)
	return encrypted_char_shift ^ 22

def rol8(encrypted_char):
	encrypted_char_bin = "{0:08b}".format(encrypted_char)
	carry_bits = encrypted_char_bin[:4]
	encrypted_char_shift = list("{0:08b}".format(encrypted_char << 8%8))

	for i in range(len(carry_bits)):
		encrypted_char_shift[i] = carry_bits[i]

	encrypted_char_shift = int(''.join(encrypted_char_shift), 2)
	return encrypted_char_shift

def decrypt():
	for encrypted_char in encrypted_flag:
		for letter in alphabet:
			decrypted_char = ror4(ord(letter))
			if hex(rol8(decrypted_char)) == hex(encrypted_char):
				flag.append(letter)
				break

decrypt()
print ''.join(flag)
