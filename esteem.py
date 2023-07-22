
def main():
	print("This program is an implementation of the Rosenberg")
	print("Self-Esteem Scale. This program will show you ten")
	print("statements that you could possibly apply to yourself.")
	print("Please rate how much you agree with each of the")
	print("statements by responding with one of these four letters:")
	print("")
	print("'D' means you strongly disagree with the statement.")
	print("'d' means you disagree with the statement.")
	print("'a' means you agree with the statement.")
	print("'A' means you strongly agree with the statement.")
	print("")

	# Initial score
	points_negative = 0
	points_positive = 0
	points = 0

	first = input("1. I feel that I am a person of worth, at least on anequal plane with others.\nEnter D, d, a, or A: ")
	second = input("2. I feel that I have a number of good qualities.\nEnter D, d, a, or A: ")
	third = input("3. All in all, I am inclined to feel that I am a failure.\nEnter D, d, a, or A: ")
	forth = input("4. I am able to do things as well as most other people.\nEnter D, d, a, or A: ")
	fifth = input("5. I feel I do not have much to be proud of.\nEnter D, d, a, or A: ")
	sixth = input("6. I take a positive attitude toward myself.\nEnter D, d, a, or A: ")
	seventh = input("7. On the whole, I am satisfied with myself.\nEnter D, d, a, or A: ")
	eighth = input("8. I wish I could have more respect for myself.\nEnter D, d, a, or A: ")
	nineth = input("9. I certainly feel useless at times.\nEnter D, d, a, or A: ")
	tenth = input("10. At times I think I am no good at all.\nEnter D, d, a, or A: ")

	compute_positve_statements(first, second, forth, sixth, seventh)
	compute_negative_statements(third, fifth, eighth, nineth, tenth)
	compute_points(points_negative, points_positive)


	print()
	print(f"Your score is {points}.")
	print("A score below 15 may indicate problematic low self-esteem.")

	# Function for statements 1, 2, 4, 6 and 7
def compute_positve_statements(first, second, forth, sixth, seventh):
	"""Add points according to the scale

	Strongly Disagree = 0
	Disagree = 1
	Agree = 2
	Strongly Agree = 3

	"""
	points_positive = 0
	if first == "d" or second == "d" or forth == "d" or sixth == "d" or seventh == "d":
		points_positive += 1
	elif first == "a" or second == "a" or forth == "a" or sixth == "a" or seventh == "a":
		points_positive += 2
	elif first == "A" or second == "A" or forth == "A" or sixth == "A" or seventh == "a":
		points_positive += 3
	else:
		points_positive += 0

	return points_positive

	# Function for statements 3, 5, 8, 9 and 10
def compute_negative_statements(third, fifth, eighth, nineth, tenth):
	"""Add points according to the scale
	
	Strongly Disagree = 3
	Disagree = 2
	Agree = 1
	Strongly Agree = 0

	"""
	points_negative = 0
	if third == "a" or fifth == "a" or eighth == "a" or nineth == "a" or tenth == "a":
		points_negative += 1
	elif third == "d" or fifth == "d" or eighth == "d" or nineth == "d" or tenth == "d":
		points_negative += 2
	elif third == "D" or fifth == "D" or eighth == "D" or nineth == "D" or tenth == "D":
		points_negative += 3
	else:
		points_negative += 0

	return points_negative

def compute_points(points_negative, points_positive):
	# Compute the sum of the points

	points = points_negative + points_positive
	return points

# Execute the program
main()