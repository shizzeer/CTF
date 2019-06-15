import string

cipher_text = "llkjmlmpadkkc"
key = "thisisalilkey"

alphabet = string.ascii_lowercase
plain_text = []
i = 0

for letter in cipher_text:
	index_of_the_plain_letter = (alphabet.index(letter) - alphabet.index(key[i])) % 26
	plain_text.append(alphabet[index_of_the_plain_letter])
	i += 1

print "".join(plain_text)
