import argparse

# Initialise the parser
parser = argparse.ArgumentParser()

# Add options 
parser.add_argument("-o", "--option", type = int, choices = [1, 2, 3], help = "Options: 1. Calculator, 2. Check if number is armstrong or not, 3. Display Fibonacci series")
parser.add_argument("-i", "--inputs", type = int, help = "Inputs for the  selected option.")

# To get the arguments as variables
args = parser.parse_args()

# Driving the menu
if args.option == 2:
	number = args.inputs
	onum = args.inputs

	temp = 0
	size = 0

	# To calculate the number of digits of the entered number
	while number != 0:
		size += 1
		number //= 10

	number = args.inputs

	# Main code to check if number is Armstrong or not
	while number != 0:
		rem = number % 10
		temp += (rem ** size)
		number //= 10

	# To tell if Armstrong
	if temp == onum:
		print("{} is an Armstrong number".format(args.inputs))

	# Number is not Armstrong
	else:
		print("{} is not an Armstrong number".format(args.inputs))