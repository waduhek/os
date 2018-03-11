import argparse

parser = argparse.ArgumentParser()

option_help = "Options: 1. Calculator, 2. Check if number is armstrong or not, 3. Display Fibonacci series"

parser.add_argument("-o", "--option", type = int, choices = [1, 2, 3], help = option_help)
parser.add_argument("-i", "--inputs", type = int, help = "Inputs for the  selected option.")

args = parser.parse_args()

if args.option == 2:
	number = args.inputs
	onum = args.inputs

	temp = 0
	size = 0

	while number != 0:
		size += 1
		number //= 10

	number = args.inputs

	while number != 0:
		rem = number % 10
		temp += (rem ** size)
		number //= 10

	if temp == onum:
		print("{} is an Armstrong number".format(args.inputs))