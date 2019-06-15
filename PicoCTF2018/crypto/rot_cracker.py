import string

cipher_text = "cvpbPGS{guvf_vf_pelcgb!}"
alphabet =  string.ascii_lowercase
plain_text = []

def decrypt(key, cipher_text):
	for letter in cipher_text:
		if letter.islower():
			plain_text.append(alphabet[(ord(letter) - ord('a') - key) % 26])
		elif letter.isupper():
			plain_text.append(alphabet[ord(letter) - ord('A') - key % 26].upper())
		else:
			plain_text.append(letter)

decrypt(13, cipher_text)
print "".join(plain_text)
