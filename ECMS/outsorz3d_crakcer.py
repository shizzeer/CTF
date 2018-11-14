import subprocess
import re
import sys
import requests

correct_idx = 0

def get_the_asm_code():
	args = 'objdump -j .text -M intel --start-address=0x6F0 -S binary > txt_code'
	process = subprocess.Popen(args, shell=True)
	process.wait()

def get_compared_values(const_code, compared_values, char_indexes):
	c_v_pattern = r'mov    BYTE PTR \[rbp-0x\w\w\],(0x\w\w)|mov    BYTE PTR \[rbp-0x\w\w\],(0x\w)'
	i = 0
	for line in const_code:
		c_v_matcher = re.search(c_v_pattern, line)
		if c_v_matcher:
			try:
				compared_values[32-i] = int(c_v_matcher.group(1), 16)
			except TypeError:
				compared_values[32-i] = int(c_v_matcher.group(2), 16)
			i += 1

def find_main_func(code):
	call_instr_pattern = r'call'
	for line in code:
		call_instr_matcher = re.search(call_instr_pattern, line)
		if call_instr_matcher:
			return line.split(':')[0][4:]

def get_char_indexes(code, char_indexes):
	i = 0
	near_main_address = find_main_func(code)
	c_idx_pattern = r'movzx  eax,BYTE PTR \[rbp-0x\w\w\]|movzx  eax,BYTE PTR \[rbp-0x\w\]'
	while True:
		if code[i].split(':')[0][4:] != near_main_address:
			i += 1
		else:
			break
	while i < len(code):
		c_idx_matcher = re.search(c_idx_pattern, code[i])
		if c_idx_matcher:
			global correct_idx
			correct_idx += 1
			if correct_idx % 2 != 0:
				char_index = c_idx_matcher.group().split('[')[1].split('-')[1][:-1]
				char_indexes.append(int(char_index, 16))
		i += 1

def get_jmp_indexes(line, jmp_list):
	local_func_indexes = []
	f_idx_pattern = r'call   (\w\w\w) <exit@plt\+0x\w\w\w>'
	f_idx_matcher = re.search(f_idx_pattern, line)
	if f_idx_matcher:
		global correct_idx
		correct_idx += 1
		if correct_idx % 2 == 0:
			jmp_list.append(f_idx_matcher.group(1))

def find_add(line):
	add_pattern = r'add\s'
	add_matcher = re.search(add_pattern, line)
	if add_matcher:
		return True
	else:
		return False

def find_sub(line):
	sub_pattern = r'sub\s'
	sub_matcher = re.search(sub_pattern, line)
	if sub_matcher:
		return True
	else:
		return False

def find_xor(line):
	xor_pattern = r'xor    al,BYTE PTR \[rbp-0x2\]'
	xor_matcher = re.search(xor_pattern, line)
	if xor_matcher:
		return True
	else:
		return False

def find_ror(line):
	ror_pattern = r'ror\s'
	ror_matcher = re.search(ror_pattern, line)
	if ror_matcher:
		return True
	else:
		return False

def find_rol(line):
	rol_pattern = r'rol\s'
	rol_matcher = re.search(rol_pattern, line)
	if rol_matcher:
		return True
	else:
		return False

def exec_add(operand, compared_value):
	return (compared_value - operand)&0xff

def exec_sub(operand, compared_value):
	return (compared_value + operand)&0xff

def exec_xor(operand, compared_value):
	for i in range(33, 127):
		if i ^ operand == compared_value:
			return i & 0xff

def exec_ror(operand, compared_value):
	ror = lambda val, r_bits, max_bits: \
	    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
	    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

	for i in range(33, 127):
		if ror(i, operand, 8) == compared_value:
			return i & 0xff

def exec_rol(operand, compared_value):
	rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

	for i in range(33, 127):
		if rol(i, operand, 8) == compared_value:
			return i & 0xff

def cracker(const_code, jmp_list, compared_values, c_idxs, flag):
	i = 0
	c_idx_counter = 0
	for index in jmp_list:
		while i < len(const_code):
			if const_code[i].split(':')[0][4:] == ' ' + index:
				break 
			i += 1
		while const_code[i][-8:] != 'ret    \n':
			operand_pattern = r'mov    BYTE PTR \[rbp-0x2\],(0x\w\w)|mov    BYTE PTR \[rbp-0x2\],(0x\w)'
			operand_matcher = re.search(operand_pattern, const_code[i])
			if operand_matcher:
				try:
					operand = int(operand_matcher.group(1), 16)
				except TypeError:
					operand = int(operand_matcher.group(2), 16)
			if find_add(const_code[i]):
				flag[32-c_idxs[c_idx_counter]] = chr(exec_add(operand, compared_values[c_idxs[c_idx_counter]]))
			elif find_sub(const_code[i]):
				flag[32-c_idxs[c_idx_counter]] = chr(exec_sub(operand, compared_values[c_idxs[c_idx_counter]]))
			elif find_xor(const_code[i]):
				flag[32-c_idxs[c_idx_counter]] = chr(exec_xor(operand, compared_values[c_idxs[c_idx_counter]]))
			elif find_ror(const_code[i]):
				flag[32-c_idxs[c_idx_counter]] = chr(exec_ror(operand, compared_values[c_idxs[c_idx_counter]]))
			elif find_rol(const_code[i]):
				flag[32-c_idxs[c_idx_counter]] = chr(exec_rol(operand, compared_values[c_idxs[c_idx_counter]]))
			i += 1
		i = 0
		c_idx_counter += 1

def download_binary():
	r = requests.get('http://outsourz3d.ecsm2018.hack.cert.pl/binary', stream=True)
	with open('binary', 'wb') as f:
		f.write(r.content)
		return r.cookies['session']
	del r

def send_the_flag(session_id, flag):
	r = requests.post('http://outsourz3d.ecsm2018.hack.cert.pl/validate', cookies={'session': session_id}, data={'answer': flag})
	if r.status_code == 200:
		print('SESSION_ID: ', r.cookies['session'])
		print(r.text)

def main():
	for k in range(20):
		compared_values = []
		char_indexes = []
		flag = []
		jmp_list = []
		const_code = []

		session_id = download_binary()
		print('download SESSION_ID:', session_id)

		for i in range(33):
			flag.append('X')
			compared_values.append(0)

		code = open('txt_code', 'w+')

		get_the_asm_code()

		for line in code.readlines():
			const_code.append(line)
			get_jmp_indexes(line, jmp_list)

		global correct_idx
		correct_idx = 0

		get_char_indexes(const_code, char_indexes)

		get_compared_values(const_code, compared_values, char_indexes)

		cracker(const_code, jmp_list, compared_values, char_indexes, flag)

		flag = ''.join(flag)[:-1]
		code.close()
		send_the_flag(session_id, flag)

if __name__ == '__main__':
	main()

