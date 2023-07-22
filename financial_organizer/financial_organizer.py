# Develop a program that helps with monthly income and spending.
# The idea is to keep track and to organize personal and family finance.
# Libraries that will be used
import datetime
import csv
import pytest
from os import system as clear
from time import sleep

DATE_INDEX = 0
NAME_INDEX = 1
VALUE_INDEX = 2

def main():
	def prog_menu():
		main_menu = True
		balance = 0
		while main_menu == True:

			clear("cls")
			print("---------------------------------------------------------------")
			print(f"Balance: ${balance}")
			print()
			print("[1] Add income")
			print("[2] Add bill")
			print("[3] Bills")
			print("[0] Exit program")
			print()
			print("---------------------------------------------------------------")
			print()

			option = int(input("Enter your option: "))

			if option == 1:
				amount = float(input("Enter an amount: $"))
				print(f"{amount} added to your balance!")
				sleep(2)
				balance += amount
			elif option == 2:
				option2(2)
			elif option == 3:
				read_bills("paidbills.csv")
				back = input("Press enter to continue.")
			elif option == 0:
				main_menu == False
				clear("cls")
				print("Program closed successfully.")
				break
			else:
				print("Invalid option")


	prog_menu()


def option1(option):
	balance = (option1)
	# Function to add income
	if option == 1:
		# add income stuff
		amount = float(input("Enter an amount: $"))
		print(f"{amount} added to your balance!")
		sleep(2)
		balance += amount
	return balance


def option2(option):
	# Function to add a bill to the list

	def add_bill(bill_date, bill_name, bill_value):
		# Add bill to the list. Input from user.
		new_bill = [bill_date, bill_name, bill_value]

		with open("paidbills.csv", "a", newline="") as f_object:

			writer_object = csv.writer(f_object)
			writer_object.writerow(new_bill)
			#f_object.close()



	if option == 2:
		bill_date = input("When are you paying that bill? (ex: 12-02-2022) ")
		while len(bill_date) != 10:
			print("Incorrect format, please try again.")
			sleep(2)
			bill_date = input("When are you paying that bill? (ex: 12-02-2022) ")
		bill_name = str(input("Give this bill a name: "))
		bill_value = float(input("How much does it cost? $"))
		add_bill(bill_date, bill_name, bill_value)
		print()
		print(f"Success! '{bill_name}' from {bill_date} that costs ${bill_value} was added!")
		sleep(2)
		return bill_value

def read_bills(filename):
	# read past paid bills from a csv file.

	bills_list = []

	# First, open the file for reading.
	with open(filename, "rt") as csv_file:

		# Second, create object reader to read
		# the opened file.
		reader = csv.reader(csv_file, delimiter=",")
		i = 0
		# Third, skip the header in the csv file.

		next(reader)

		# Forth, process the rows in the file.
		for row in reader:

			# fifth, append what was read to the end of the list.
			bills_list.append(row)

		for i in bills_list:
			print(bills_list[1])
			i += 1
			
	# return the list
	return bills_list

if __name__ == "__main__":
    main()