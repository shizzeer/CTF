import struct

encrypted_password = '7b 18 a6 36 da 3b 2b a6 fe cb 82 ae 96 ff 9f 46 8f 36 a7 af fe 93 8e 3f \
46 a7 ff 82 cf ce b3 97 17 1a a7 36 ef 2b 8a ed 00'.replace(' ', '').decode('hex')

# from https://gist.github.com/trietptm/5cd60ed6add5adad6a34098ce255949a
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
	((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
	(val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def encrypt(password):
	b_password = bytearray(b_password)
	for i in range(len(b_password) - 3):
		b_password[i] ^= 0x9d # XOR Byte

		word_to_encrypt = struct.unpack('<H', b_password[i:i+2])[0]	# This instruction takes two bytes from b_password[i]
		word_to_encrypt = ror(word_to_encrypt, 0x5, 16)				
		b_password[i:i+2] = bytearray(struct.pack('<H', word_to_encrypt)) # Set b_password[i:i+2] to the new encrypted value 

		dword_to_encrypt = struct.unpack('<I', b_password[i:i+4])[0] # This instruction takes four bytes from b_password[i]
		dword_to_encrypt = rol(dword_to_encrypt, 0xb, 32)
		b_password[i:i+4] = bytearray(struct.pack('<I', dword_to_encrypt)) # Set b_password[i:i+4] to the new encrypted value

	print str(b_encrypted_password)

def decrypt(encrypted_password):
	'''
		This function is decryption. It go through the end of encrypted_password to the beginning and does the opposite 
		operations to the encrypt function.
	'''
	b_encrypted_password = bytearray(encrypted_password)
	for i in range(len(b_encrypted_password) - 5, -1, -1):
		word_to_decrypt = struct.unpack('<I', b_encrypted_password[i:i+4])[0]
		word_to_decrypt = ror(word_to_decrypt, 0xb, 32)
		b_encrypted_password[i:i+4] = struct.pack('<I', word_to_decrypt)

		dword_to_decrypt = struct.unpack('<H', b_encrypted_password[i:i+2])[0]
		dword_to_decrypt = rol(dword_to_decrypt, 0x5, 16)
		b_encrypted_password[i:i+2] = struct.pack('<H', dword_to_decrypt)

		b_encrypted_password[i] ^= 0x9d

	print str(b_encrypted_password)


decrypt(encrypted_password)
