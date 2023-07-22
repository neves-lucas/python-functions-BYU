# Create a list of numbers, appends more numbers onto the list, and prints the list.
# The program must have two functions named main and append_random_numbers.
import random

def main():
	"""
	A) Has no parameters.
	B) Creates a list named numbers.
	C) Prints the numbers list
	D) Calls the append_random_numbers function with only one argument to add one number to numbers
	E) Prints the numbers list
	F) Calls the append_random_numbers function again with two arguments to add three numbers to numbers
	G) Prints the numbers list
	"""
	numbers = [16.2, 75.1, 52.3]
	print(numbers)
	append_random_numbers(numbers)
	print(numbers)
	append_random_numbers(numbers, 3)
	print(numbers)



def append_random_numbers(alist, quantity=1):
	"""
	A) Has two parameters: a list named numbers_list and an integer named quantity. The parameter quantity has a default value of 1
	B) Computes quantity pseudo random numbers by calling the random.uniform function.
	C) Rounds the quantity pseudo random numbers to one digit after the decimal.
	D) Appends the quantity pseudo random numbers onto the end of the numbers_list.
	
	"""
	i = 0
	while i != quantity:
		numbers_to_append = random.uniform(10, 100)
		numbers_to_append = round(numbers_to_append, 1)
		alist.append(numbers_to_append)
		i += 1

main()