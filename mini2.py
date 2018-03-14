# Add shebang here

import os 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("option", type = int, choices = [1, 2, 3, 4, 5, 6], help = "Options: 1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Modulo, 6. Factorial")
parser.add_argument("input", type = int, help = "Compulsory input for the calculator.")
parser.add_argument("-i", "--input2", type = int, help ="Second input for the calculator")

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

args = parser.parse_args()

pid = os.fork()

if args.option == 1:
	if pid == 0:
		print("The sum of {} and {} is {}".format(args.input, args.input2, add(args.input, args.input2)))

		os._exit(0)

	elif pid < 0:
		print("Child process could not be created!")

	else:
		os.wait()
