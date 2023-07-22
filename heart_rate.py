"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

# First get the user's age.
age = input("Please enter your age: ")

# Second comput the slowest and fastest rates
maximum_rate = 220 - int(age)
slowest = maximum_rate * .65
fastest = maximum_rate * .85

# Output results

print(f"When you exercise to strenghten your heart, you should keep your heart rate between {slowest:.2f} and {fastest:.2f} beats per minute.")