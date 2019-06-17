plain_text = []

def decrypt(key, cipher_text):
	for letter in cipher_text:
		plain_text.append(chr((ord(letter) + key) % 255))
	print ("".join(plain_text))

decrypt(11, "e^Xd8I;pX6ZhVGT8^E]:gHT_jHITVG:cITh:XJg:r")
