#!/usr/bin/python3
import re

def find_indexes():
	with open('checkFlag_code.txt', 'r') as checkFlag_code:
		pattern = r'\s(\d|\d\d)\s'
		indexes = re.findall(pattern, str(checkFlag_code.read()))
		indexes = [index for index in indexes if index != '0']
		print('-------------- INDEXES ----------------\n')
		print('\t'.join(indexes))
		return indexes

def find_chars():
	with open('checkFlag_code.txt', 'r') as checkFlag_code:
		pattern = r'\'(\S{1})\''
		chars = re.findall(pattern, str(checkFlag_code.read()))
		print('-------------- CHARS ----------------\n')
		print('\t'.join(chars))
		return chars

def crack_the_password(indexes, chars):
	password = []
	i = 0
	for k in range(50):
		password.append('$')
	for j in range(len(indexes)):
		password[int(indexes[j])] = chars[i]
		i += 1
	password[0] = 'p'
	password = [char for char in password if char != '$']
	print('\n' + ''.join(password))

def main():
	indexes = find_indexes()
	chars = find_chars()
	crack_the_password(indexes, chars)

if __name__ == '__main__':
    main()
