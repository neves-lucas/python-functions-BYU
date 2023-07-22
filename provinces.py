with open("provinces.txt", "rt") as provinces_file:

	provinces = []

	for line in provinces_file:
		clean_line = line.strip()
		provinces.append(clean_line)


	print(provinces)