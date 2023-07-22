'''
Write a Python program named tire_volume.py that reads
from the keyboard the three numbers for a tire and computes 
and outputs the volume of space inside that tire.
'''

from math import pi
import datetime
from unittest import skip

# Standard variables for exceeding requirements.
phone = ""
price = 0

# Inputs to gather data
width = input("Enter the width of the tire in mm (ex 205): ")
aspect_ratio = input("Enter the aspect ratio of the tire (ex 60): ")
diameter = input("Enter the diameter of the wheel in inches (ex 15): ")

# Computation
volume = pi * int(width) ** 2 * int(aspect_ratio) * (int(width) * int(aspect_ratio) + 2540 * int(diameter)) / 10000000000

# Prices for exceeding requirements.
# Source: https://www.walmart.com/browse/auto-tires/passenger-car-tires/91083_1077064_1063465
if int(aspect_ratio) <= 205 and int(width) >= 65 and int(diameter) <=16:
  price = 100
elif int(aspect_ratio) <= 215 and int(width) >= 55 and int(diameter) <= 16:
  price = 106
elif int(aspect_ratio) <= 215 and int(width) >= 55 and int(diameter) == 17:
  price = 131
elif int(aspect_ratio) <= 245 and int(width) >= 50 and int(diameter) == 20:
  price = 163
else:
  price = 0

print(f"The approximate volume is {volume:.2f}")
print(f"The price for this tire is: ${price}")

# Asking is the user wants to buy the tire. (exceeding requirements)
sell = input("You want to buy this tire?  [Y/N]")
if sell.lower() == "n":
  print("Well, then have a great day!")
elif sell.lower() == "y":
  phone = input("Please enter your phone number so we can call you: ")
else:
  skip

# Prove assignment
# Gets the current date from the computer's operating system.
date = datetime.date.today()

# Opens a text file name volumes.txt for appending.
with open ("volumes.txt", "at") as volumes_file:
  print(f"{date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone}", file=volumes_file)
