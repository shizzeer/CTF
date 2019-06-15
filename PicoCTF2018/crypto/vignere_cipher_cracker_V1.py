import string

cipher_text = "llkjmlmpadkkc"
key = "thisisalilkey"

table = open("table.txt", "r")
cipher_data = []

for line in table:
	line = line.replace(" ", "").replace("\n", "").replace("|", "")
	cipher_data.append(line)


cipher_text_idx = 0
alphabet = string.ascii_lowercase
plain_text = []

for letter in key:
	for data_to_decrypt in cipher_data:
		if data_to_decrypt[0] == letter.upper():
			for i in range(1, 27):
				if data_to_decrypt[i] == cipher_text[cipher_text_idx].upper():
					plain_text.append(alphabet[i - 1])
					break
			break
	cipher_text_idx += 1

print "".join(plain_text)
