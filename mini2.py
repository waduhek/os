#!/home/bin/python3

import os 
import argparse

# Initialise the parser
parser = argparse.ArgumentParser()

# Add positional and optional arguments
parser.add_argument("option", type = int, choices = [1, 2, 3, 4, 5, 6], help = "Options: 1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Modulo, 6. Factorial")
parser.add_argument("input", type = int, help = "Compulsory input for the calculator.")
parser.add_argument("input2", type = int, help ="Second input for the calculator (If not needed put a 0)")
parser.add_argument("-i3", type = int, help = "Use if 2 operations are to be performed at the same time.(Do not use for factorial)")
parser.add_argument("-i4", type = int, help = "Use if 2 operations are to be performed at the same time.(Do not use for factorial)")

# Utility functions for driving the calculator
def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def modulo(a, b):
	return a % b

def divide(a, b):
	return a / b

def factorial(a):
	result = 1

	for i in range(1, a + 1):
		result *= i

	return result

# Get arguments as variables
args = parser.parse_args()

# Create a child process
pid = os.fork()

# Child process could not be created
if pid < 0:
	print("Child process could not be created!")

# Child process was successfully created
elif pid == 0:
	# Check if optional inputs were provided or not
	try:
		# Perform addtion
		if args.option == 1:
			print("The sum of {} and {} is {}".format(args.i3, args.i4, add(args.i3, args.i4)))

			os._exit(0)

		# Perform subtraction
		elif args.option == 2:
			print("The difference between {} and {} is {}".format(args.i3, args.i4, subtract(args.i3, args.i4)))

			os._exit(0)

		# Perform multiplication
		elif args.option == 3:
			print("The product of {} and {} is {}".format(args.i3, args.i4, multiply(args.i3, args.i4)))

			os._exit(0)

		# Perform division
		elif args.option == 4:
			# Check for division by 0
			try:
				print("The result of dividing {} by {} is {}".format(args.i3, args.i4, divide(args.i3, args.i4)))

				os._exit(0)

			# Handle ZeroDivisionError if 0 is the divisor
			except ArithmeticError:
				print("Illegal division!")

				os._exit(0)

		# Perform modulo
		elif args.option == 5:
			try:
				print("The remainder of dividing {} by {} is {}".format(args.i3, args.i4, modulo(args.i3, args.i4)))

				os._exit(0)

			except ArithmeticError:
				print("Illegal operation!")

				os._exit(0)

		# Find the factorial
		elif args.option == 6:
			# Since 'input2' is a positional input, some input is needed
			# If user enters 0 the second factorial is not calculated
			if args.input2 != 0:
				print("The factorial of {} is {}".format(args.input2, factorial(args.input2)))

				os._exit(0)

			else:
				os._exit(0)

	# Handle the exception raised if the optional inputs are not present which will be NoneTypeError
	except TypeError:
		os._exit(0)

# Still in parent process
# Perform the same tasks as above
else: 
	if args.option == 1:
		print("The sum of {} and {} is {}".format(args.input, args.input2, add(args.input, args.input2)))

		os.wait()

	elif args.option == 2:
		print("The difference between {} and {} is {}".format(args.input, args.input2, subtract(args.input, args.input2)))

		os.wait()

	elif args.option == 3:
		print("The product of {} and {} is {}".format(args.input, args.input2, multiply(args.input, args.input2)))

		os.wait()

	elif args.option == 4:
		try:
			print("The result of dividing {} by {} is {}".format(args.input, args.input2, divide(args.input, args.input2)))

			os.wait()

		except ArithmeticError:
			print("Illegal division!")

			os.wait()

	elif args.option == 5:
		try:
			print("The remainder of dividing {} by {} is {}".format(args.input, args.input2, modulo(args.input, args.input2)))

			os.wait()

		except ArithmeticError:
			print("Illegal operation!")

			os.wait()

	elif args.option == 6:
		print("The factorial of {} is {}".format(args.input, factorial(args.input)))

		os.wait()

	else:
		os.wait()


