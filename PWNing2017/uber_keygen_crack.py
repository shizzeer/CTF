#!/usr/bin/python3
import re

index = 0
bit_to_check = 0
bit_to_check_is_one = 0
bits_counter = 0
password = ['X']*50
ascii_of_the_char = 1

def find_index(line):
	index_assembly_instr_pattern = r'add'
	index_assembly_instr_match = re.search(index_assembly_instr_pattern, line)
	if index_assembly_instr_match:
		hex_index_pattern = r'\s(\w\w[h])\s'
		hex_index_match = re.search(hex_index_pattern, line)
		if hex_index_match:
			global index 
			index = int(''.join(hex_index_match.group(1).split('h')[0:1]), 16)
		else:
			dec_index_pattern = r'\s(\d)\s'
			dec_index_match = re.search(dec_index_pattern, line)
			index = int(dec_index_match.group(1))

def find_bit_to_check(line):
	sar_assembly_instr_pattern = r'sar'
	sar_assembly_instr_match = re.search(sar_assembly_instr_pattern, line)
	if sar_assembly_instr_match:	
		sar_value_pattern = r'\s(\d)\s'
		sar_value_match = re.search(sar_value_pattern, line)
		global bit_to_check
		bit_to_check = int(sar_value_match.group(1))

def find_if_bit_is_one(line):
	cmp_assembly_instr_pattern = r'cmp'
	cmp_assembly_instr_match = re.search(cmp_assembly_instr_pattern, line)
	if cmp_assembly_instr_match:
		global bits_counter
		bits_counter += 1
		if bits_counter > 8:
			bits_counter = 1
		cmp_value_pattern = r'\s(\d)\s'
		cmp_value_match = re.search(cmp_value_pattern, line)
		global bit_to_check_is_one_or_zero
		bit_to_check_is_one_or_zero = int(cmp_value_match.group(1))
		crack_the_password(bit_to_check_is_one_or_zero, bit_to_check, index)
		
def crack_the_password(bit_to_check_is_one, bit_to_check, index):
	global ascii_of_the_char
	if bit_to_check_is_one and bit_to_check and bits_counter > 1:
		ascii_of_the_char += (1 << bit_to_check)
		password[index] = chr(ascii_of_the_char)
	if bits_counter == 1 and bit_to_check_is_one:
		ascii_of_the_char = 1
	elif bits_counter == 1 and not bit_to_check_is_one:
		ascii_of_the_char = 0

def main():
	with open('code_flag.txt', 'r') as checkFlag_code:
		lines = checkFlag_code.readlines()
		for line in lines:
			find_index(line)
			find_bit_to_check(line)
			find_if_bit_is_one(line)
		global password
		password[0] = 'p'
		password = [char for char in password if char != 'X']
		print('FLAG: ', ''.join(password))

if __name__ == '__main__':
    main()
