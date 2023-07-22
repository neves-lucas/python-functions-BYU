# Practice dictionaries

bad_guys = {
	'daredevil' : 'kingpin',
	'x-men': 'apocalypse',
	'batman': 'bane'
}

bad_guys['batman']
# result should be "bane"

bad_guys['deadpool'] = 'evil deadpool'
# This should assign it to our dictionary
# The same can be done to update an entry

bad_guys.pop('x-men')
# This would remove "x-men" and "apocalypse" from the dictionary

name = bad_guys['x-men']

print(bad_guys)
print(name)