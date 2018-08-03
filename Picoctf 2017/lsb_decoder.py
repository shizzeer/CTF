#!/usr/bin/python3

def get_a_flag(last_significant_bits):
	flag = []
	i = 0
	while i < len(last_significant_bits):
		byte = ''.join(last_significant_bits[i:i+8])
		flag.append(chr(int(byte,2)))
		i += 8
		if int(byte, 2) == 255:
			break

	flag = flag[:-1]
	return flag


def get_last_significant_bit(pixel):
	return (pixel & 1)

def main():
	picture_in_bytes = bytearray(open("littleschoolbus.bmp", "rb").read())
	pixels = picture_in_bytes[0x36:]


	last_significant_bits = []

	for pixel in pixels:
		last_significant_bit = str(get_last_significant_bit(pixel))
		last_significant_bits.append(last_significant_bit)

	flag = get_a_flag(last_significant_bits)

	print(''.join(flag))


if __name__ == '__main__':
	main()
