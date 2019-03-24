import string

def specific_ord(char):
		return ord(char) - 0x37

def main():
	alphabet = string.uppercase
	for letter in alphabet:
		if specific_ord(letter) == 0x1c:
			print 'Last character is: '  + letter
			print 'ABCDEFGHIJKLMNO' + letter

main()
