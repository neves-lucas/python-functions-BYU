def main():
	# Create and print a list named fruit.
	fruit_list = ["pear", "banana", "apple", "mango"]
	print(f"original: {fruit_list}")

	fruit_list.reverse()
	print(f"reversed: {fruit_list}")

	fruit_list.append("orange")
	print(f"orange appended: {fruit_list}")

	fruit_list.insert(2, "cherry")
	print(f"cherry inserted: {fruit_list}")

	fruit_list.remove("banana")
	print(f"banana removed: {fruit_list}")

	fruit_list.pop()
	print(f"popped list: {fruit_list}")

	fruit_list.sort()
	print(f"sorted list: {fruit_list}")

	fruit_list.clear()
	print(f"cleared list: {fruit_list}")

main()