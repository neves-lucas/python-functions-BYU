"""
Work as a team to write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes. Then visually examine the output and answer this question, "Which can size has the highest storage efficiency?"

Name	Radius
(centimeters)	Height
(centimeters)	Cost per Can
(U.S. dollars)
#1 	Picnic	6.83	10.16	$0.28
#1 	Tall	7.78	11.91	$0.43
#2			8.73	11.59	$0.45
#2.5		10.32	11.91	$0.61
#3 	Cylinder10.79	17.78	$0.86
#5			13.02	14.29	$0.83
#6Z			5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10			15.72	17.78	$1.53
#211		6.83	12.38	$0.34
#300		7.62	11.27	$0.38
#303		8.10	11.11	$0.42

"""
# Import Pi from the math library to do the computations.
from math import pi

def main():
	# Lists with the values that will be used
	names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "6Z", "#8Z short", "#10", "#211", "#300", "#303"]
	radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
	heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
	costs_per_can = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

	# Call the volume and surface area functions and store them in variables called "vol" and "surf_area".
	vol = compute_volume(radius[radio], heights[height])
	surf_area = compute_surface_area(radius, heights)
	storage_efficiency = surf_area / vol

	for name in names:
		for radio in radius:
			for height in heights:
				if name < [12]:
					print(f"{names[name]} {storage_efficiency}")


def compute_volume(radius, heights):
	# Computes the volume of a cylinder.
	vol = pi * (radius ** 2) * heights
	return vol

def compute_surface_area(radius, heights):
	# Computes the amount of steel needed.
	surf_area = 2 * pi * radius * (radius + heights)
	return surf_area

	

# Start the program
main()