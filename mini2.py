#!/home/bin/python3

import os 
import argparse
from random import randint

# Initialise the parser
parser = argparse.ArgumentParser()

# Add positional and optional arguments
parser.add_argument("option", type = int, choices = [1, 2, 3, 4, 5, 6], help = "Options: 1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Modulo, 6. Factorial")
parser.add_argument("input", type = int, help = "Compulsory input for the calculator.")
parser.add_argument("input2", type = int, help ="Second input for the calculator (Put 0 for factorial calculation).")

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

# Generate a random number and assign it to a flag variable
if randint(0, 3) > 0:
	k = 1

else:
	k = 0

# Create a child process only if the optional inputs are present
# Request to create a child process
pid = os.fork()

# Child process could not be created
if pid < 0:
	print("Child process could not be created!")


# Child process was successfully created
if pid == 0 and k == 0:
	print("\nThe returned value from fork is:", pid)
	print("The process ID is:", os.getpid())

	# Check if optional inputs were provided or not
	try:
		# Perform addtion
		if args.option == 1:
			print("The sum of {} and {} is {}.".format(args.input, args.input2, add(args.input, args.input2)))
			os._exit(0)

		# Perform subtraction
		elif args.option == 2:
			print("The difference between {} and {} is {}.".format(args.input, args.input2, subtract(args.input, args.input2)))

			os._exit(0)

		# Perform multiplication
		elif args.option == 3:
			print("The product of {} and {} is {}.".format(args.input, args.input2, multiply(args.input, args.input2)))

			os._exit(0)

		# Perform division
		elif args.option == 4:
			# Check for division by 0
			try:
				print("The result of dividing {} by {} is {}.".format(args.input, args.input2, divide(args.input, args.input2)))

				os._exit(0)

			# Handle ZeroDivisionError if 0 is the divisor
			except ArithmeticError:
				print("Illegal division!")

				os._exit(0)

		# Perform modulo
		elif args.option == 5:
			try:
				print("The remainder of dividing {} by {} is {}.".format(args.input, args.input2, modulo(args.input, args.input2)))

				os._exit(0)

			except ArithmeticError:
				print("Illegal operation!")

				os._exit(0)

		# Find the factorial
		elif args.option == 6:
			print("The factorial of {} is {}.".format(args.input, factorial(args.input)))

			os._exit(0)

	# Handle the exception raised if the optional inputs are not present
	# Exception raised will be NoneTypeError
	except TypeError:
		print("Since no inputs are provided, operation was performed by the parent process.")

		os._exit(0)

# Still in parent process
# Perform the same tasks as above
if pid > 0 and k == 1:
	print("\nThe value returned from fork is:", pid)
	print("The process ID is:", os.getpid())

	if args.option == 1:
		print("The sum of {} and {} is {}.".format(args.input, args.input2, add(args.input, args.input2)))

		# Check if child process was created or not
		# Do the same for the rest of the rest of the options
		try:
			if k == 0:
				os.wait()

		except ChildProcessError:
			os._exit(0)

	elif args.option == 2:
		print("The difference between {} and {} is {}.".format(args.input, args.input2, subtract(args.input, args.input2)))

		try:
			if k == 0:
				os.wait()

		except ChildProcessError:
			os._exit(0)

	elif args.option == 3:
		print("The product of {} and {} is {}.".format(args.input, args.input2, multiply(args.input, args.input2)))

		try:
			if k == 0:
				os.wait()

		except ChildProcessError:
			os._exit(0)

	elif args.option == 4:
		try:
			print("The result of dividing {} by {} is {}.".format(args.input, args.input2, divide(args.input, args.input2)))

			try:
				if k == 0:
					os.wait()

			except ChildProcessError:
				os._exit(0)

		except ArithmeticError:
			print("Illegal division!")

			try:
				if k == 0:
					os.wait()

			except ChildProcessError:
				os._exit(0)

	elif args.option == 5:
		try:
			print("The remainder of dividing {} by {} is {}.".format(args.input, args.input2, modulo(args.input, args.input2)))

			try:
				if k == 0:
					os.wait()

			except ChildProcessError:
				os._exit(0)

		except ArithmeticError:
			print("Illegal operation!")

			os.wait()

	elif args.option == 6:
		print("The factorial of {} is {}.".format(args.input, factorial(args.input)))

		try:
			if k == 0:
				os.wait()

		except ChildProcessError:
			os._exit(0)

	else:
		try:
			if k == 0:
				os.wait()

		except ChildProcessError:
			os._exit(0)


