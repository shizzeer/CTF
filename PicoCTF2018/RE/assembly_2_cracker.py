def asm2(first_arg, second_arg):
	while first_arg <= 0x8f90:
		second_arg += 1
		first_arg += 0x8f

	print hex(second_arg)

asm2(0x6, 0x28)
