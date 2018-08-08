#/usr/bin/python3

def main():

	KEYPAD_USB_PAGE = {
		'04': 'a',
		'05': 'b',
		'06': 'c',
		'07': 'd',
		'08': 'e',
		'09': 'f',
		'0a': 'g',
		'0b': 'h',
		'0c': 'i',
		'0d': 'j',
		'0e': 'k',
		'0f': 'l',
		'10': 'm',
		'11': 'n',
		'12': 'o',
		'13': 'p',
		'14': 'q',
		'15': 'r',
		'16': 's',
		'17': 't',
		'18': 'u',
		'19': 'v',
		'1a': 'w',
		'1b': 'x',
		'1c': 'y',
		'1d': 'z',
		'1e': '1',
		'1f': '2',
		'20': '3',
		'21': '4',
		'22': '5',
		'23': '6',
		'24': '7',
		'25': '8',
		'26': '9',
		'27': '0',
		'2d': '_',
		'2f': '{',
		'30': '}'
	}
	
	flag = []

	with open("captured_usb_data.txt", "r") as captured_usb_data_file:
		captured_usb_data = captured_usb_data_file.readlines()
		for line in captured_usb_data:
			hex_id = line.split(':')[2]
			encoded_char = KEYPAD_USB_PAGE.get(hex_id)
			if encoded_char != None:
				flag.append(encoded_char)

	print(''.join(flag))

if __name__ == '__main__':
    main()
