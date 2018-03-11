import argparse

# Initialise the parser
parser = argparse.ArgumentParser()

# Add postional and optional arguments
parser.add_argument("option", type = int, choices = [1, 2, 3], help = "Options: 1. Calculator, 2. Check if number is armstrong or not, 3. Display Fibonacci series")
parser.add_argument("input", type = int, help = "Input for the  selected option.")
parser.add_argument("-c", "--calc_option", type = int, choices = [1, 2, 3, 4], help = "Calculator options: 1. Add, 2. Subtract, 3. Multiply, 4. Divide")
parser.add_argument("-i2", "--input2", type = int, help = "Use for inputing the second number to the calculator.")

# To get the arguments as variables
args = parser.parse_args()

# Driving the menu

# Check if entered number is Armstrong or not
if args.option == 2:
	number = args.input
	onum = args.input

	temp = 0
	size = 0

	# To calculate the number of digits of the entered number
	while number != 0:
		size += 1
		number //= 10

	number = args.input

	# Main code to check if number is Armstrong or not
	while number != 0:
		rem = number % 10
		temp += (rem ** size)
		number //= 10

	# To tell if Armstrong
	if temp == onum:
		print("{} is an Armstrong number".format(args.input))

	# Number is not Armstrong
	else:
		print("{} is not an Armstrong number".format(args.input))

# Print Fibonacci series upto entered number
elif args.option == 3:
	count = args.input
	n1 = 0
	n2 = 1
	i = 0

	print("Fibonacci series upto {} terms:".format(args.input))

	# Calculate the series
	while i < count:
		print(n1, end = ', ')
		nth = n1 + n2
		n1 = n2
		n2 = nth

		i += 1

	print()


else:
	# Calculate the sum of the numbers
	if args.calc_option == 1:
		result = args.input + args.input2

		print("The sum of {} and {} is {}".format(args.input, args.input2, result))

	# Calculate the difference between the numbers
	elif args.calc_option == 2:
		result = args.input - args.input2

		print("The difference between {} and {} is {}".format(args.input, args.input2, result))

	# Calculate the product of the  numbers
	elif args.calc_option == 3:
		result = args.input * args.input2

		print("The product of {} and {} is {}".format(args.input, args.input2, result))

	# Calculate the results of division
	else:
		quo = args.input // args.input2
		rem = args.input % args.input2

		print("{} divided by {} gives: Quotient = {} and Remainder = {}".format(args.input, args.input2, quo, rem))

