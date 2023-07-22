import csv
from datetime import time, datetime

# Indexes of the columns in request.csv
PRODUCT_NUMBER_INDEX = 0
QUANTITY_INDEX = 1
filename = "products.csv"

def main():
    try:
        products_dict = read_dict(filename, 0)
        print("Greengrocer")
        print()
        with open("request.csv", "r") as request_file:
            csv_reader = csv.reader(request_file)
            next(csv_reader)
            total_nums = []
            subtotal = []
            sales_tax = 0

            for row in csv_reader:
                product_number = row[PRODUCT_NUMBER_INDEX]
                quantity = row[QUANTITY_INDEX]
                tax = 0.06
                discount_percent = 0.1
                products_list = products_dict.get(product_number)
                if product_number == products_list[0]:
                    print(f"{products_list[1]}: {quantity} @ {products_list[2]}")
                    total_nums.append(int(quantity))
                    subtotal_sum = int(quantity) * float(products_list[2])
                    subtotal.append(subtotal_sum)

            total_num = sum(total_nums)
            subtotal = sum(subtotal)
            sales_tax = subtotal * tax
            discount_day = subtotal * discount_percent
            total = subtotal + sales_tax
            total_discount_day = total - discount_day
            total_discount_day_hour = total - discount_day - discount_day
            weekday = datetime.today().weekday()
            time = datetime.now() 

            print()        
            print(f"Number of items: {total_num}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales tax: {sales_tax:.2f}")
            print(f"Total: {total:.2f}")
            if weekday == 1 or weekday == 2:
                print()
                print("Today we have a 10% discount!")
                print(f"Total after discount: {total_discount_day:.2f}")
            elif time.hour <= 11:
                print()
                print("Early in the morning we have a 10% discount!")
                print(f"Total after discount: {total_discount_day_hour:.2f}")
            else:
                print(f"Total: {total:.2f}")

            print()
            print("Thank you for shopping at Greengrocer")
            current_date_and_time = datetime.now()
            print(f"{current_date_and_time:%A %I:%M %p}")

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file '{filename}' doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")

    except PermissionError as permiss_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(permiss_err).__name__, permiss_err, sep=": ")
        print(f"You're not allowed to open {filename}.")
        print("Run the program again with proper permissions.")

    except KeyError as key_err:
        print()
        print(type(key_err).__name__, key_err, sep=": ")
        print('Key Not Found')
    



def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    
    dictionary = {}
    with open(filename, "r") as products:
        csv_reader = csv.reader(products)
        next(csv_reader)
        for row in csv_reader:
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row

    return dictionary

main()