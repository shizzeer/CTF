def main():
	flag = []
	secret_buffer = [0x29, 0x6, 0x16, 0x4F, 0x2b, 0x35, 0x30, 0x1e, 0x51, 0x1b, 0x5b, 0x14, 0x4b, 0x8, 0x5d, 
					0x2b, 0x5c, 0x10, 0x6, 0x6, 0x18, 0x45, 0x51, 0x0, 0x5d]

	greeting_message = "You have now entered the "

	for i in range(len(secret_buffer)):
		flag.append((chr(ord(greeting_message[i]) ^ secret_buffer[i])))

	print ''.join(flag)

main()
