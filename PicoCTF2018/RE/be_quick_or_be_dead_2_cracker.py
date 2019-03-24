import sys
import numpy as np

def fib(number):
	fib_numbers = [0, 1]
	if number == 0:
		print fib_numbers[0]
	elif number == 1:
		print fib_numbers[1]
	else:
		i = 0
		while number != 0:
			fib_numbers.append(np.uint32(fib_numbers[i] + fib_numbers[i + 1]))
			i += 1
			number -= 1
		print fib_numbers[i]

fib(int(sys.argv[1]))
