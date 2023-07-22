import math
# 1st Ask for the number of manufactured items
items = int(input("Enter the number of items: "))

# 2nd Ask for the number of items in each box
box = int(input("Enter the number of items per box: "))

# 3rd Compute and display the result
result = math.ceil(items/box)
print(f"For {items} items, packing {box} items in each box, you will need {result} boxes.")