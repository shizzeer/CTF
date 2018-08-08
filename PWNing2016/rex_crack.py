#!/usr/bin/python
import gdb
import string

flag = ""
gdb.execute("break *0x80487b2")	# failure branch

for i in range(26):
	for character in string.printable:
		potential_flag = flag + character
		print("potential_flag: ", potential_flag)
		with open("input.txt", "w") as output_file:
			output_file.write(potential_flag)
		try:
			gdb.execute("r < input.txt")
			gdb.execute("continue")		# we hit the breakpoint so our char is bad
			print("hit the breakpoint!")
			continue
		except:
			flag = potential_flag
			print("our flag is now: ", flag)
                            break
