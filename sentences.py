import random

def main():
	i = 0
	for i in range(6):
		quantity = 1

		if i == 0:
			tense = "past"
		elif i == 3:
			tense = "past"
		elif i == 1:
			tense = "present"
		elif i == 4:
			tense = "present"
		else:
			tense = "future"


		if i <= 2:
			quantity = 1
			determiner = get_determiner(quantity)
			noun = get_noun(quantity)
			verb = get_verb(quantity, tense)
			prepositional_phrase = get_prepositional_phrase(quantity)
			print(f"{determiner} {noun} {verb} {prepositional_phrase} {noun}.")
		else:
			quantity = 0
			determiner = get_determiner(quantity)
			noun = get_noun(quantity)
			verb = get_verb(quantity, tense)
			prepositional_phrase = get_prepositional_phrase(quantity)
			print(f"{determiner} {noun} {verb} {prepositional_phrase} {noun}.")
	i += 1

def get_determiner(quantity):
	"""Return a randomly chosen determiner. A determiner is
	a word like "the", "a", "one", "some", "many".
	If quantity == 1, this function will return either "a",
	"one", or "the". Otherwise this function will return
	either "some", "many", or "the".

	Parameter
		quantity: an integer.
			If quantity == 1, this function will return a
			determiner for a single noun. Otherwise this
			function will return a determiner for a plural
			noun.
	Return: a randomly chosen determiner.
	"""
	if quantity == 1:
		words = ["a", "one", "the"]
	else:
		words = ["some", "many", "the"]

	# Randomly choose and return a determiner.
	word = random.choice(words)
	return word


def get_noun(quantity):
	"""Return a randomly chosen noun.
	If quantity == 1, this function will
	return one of these ten single nouns:
		"bird", "boy", "car", "cat", "child",
		"dog", "girl", "man", "rabbit", "woman"
	Otherwise, this function will return one of
	these ten plural nouns:
		"birds", "boys", "cars", "cats", "children",
		"dogs", "girls", "men", "rabbits", "women"

	Parameter
		quantity: an integer that determines if
			the returned noun is single or plural.
	Return: a randomly chosen noun.
	"""
	if quantity == 1:
		words = ["bird", "boy", "car", "cat", "child",
		"dog", "girl", "man", "rabbit", "woman"]
	else:
		words = ["birds", "boys", "cars", "cats", "children",
		"dogs", "girls", "men", "rabbits", "women"]

	# Randomly choose and return a noun.
	word = random.choice(words)
	return word


def get_verb(quantity, tense):
	"""Return a randomly chosen verb. If tense is "past",
	this function will return one of these ten verbs:
		"drank", "ate", "grew", "laughed", "thought",
		"ran", "slept", "talked", "walked", "wrote"
	If tense is "present" and quantity is 1, this
	function will return one of these ten verbs:
		"drinks", "eats", "grows", "laughs", "thinks",
		"runs", "sleeps", "talks", "walks", "writes"
	If tense is "present" and quantity is NOT 1,
	this function will return one of these ten verbs:
		"drink", "eat", "grow", "laugh", "think",
		"run", "sleep", "talk", "walk", "write"
	If tense is "future", this function will return one of
	these ten verbs:
		"will drink", "will eat", "will grow", "will laugh",
		"will think", "will run", "will sleep", "will talk",
		"will walk", "will write"

	Parameters
		quantity: an integer that determines if the
			returned verb is single or plural.
		tense: a string that determines the verb conjugation,
			either "past", "present" or "future".
	Return: a randomly chosen verb.
	"""
	if tense == "past":
		words = ["drank", "ate", "grew", "laughed", "thought",
		"ran", "slept", "talked", "walked", "wrote"]
	elif tense == "present":
		if quantity == 1:
			words = ["drinks", "eats", "grows", "laughs", "thinks",
			"runs", "sleeps", "talks", "walks", "writes"]
		else:
			words = ["drink", "eat", "grow", "laugh", "think",
		"run", "sleep", "talk", "walk", "write"]
		tense == "future"
	else:
		tense == "future"
		words = ["will drink", "will eat", "will grow", "will laugh",
		"will think", "will run", "will sleep", "will talk",
		"will walk", "will write"]


	# Randomly choose and return a verb
	word = random.choice(words)
	return word

def get_preposition():
	"""Return a randomly chosen preposition
	from this list of prepositions:
		"about", "above", "across", "after", "along",
		"around", "at", "before", "behind", "below",
		"beyond", "by", "despite", "except", "for",
		"from", "in", "into", "near", "of",
		"off", "on", "onto", "out", "over",
		"past", "to", "under", "with", "without"

	Return: a randomly chosen preposition.
	"""
	words = ["about", "above", "across", "after", "along",
		"around", "at", "before", "behind", "below",
		"beyond", "by", "despite", "except", "for",
		"from", "in", "into", "near", "of",
		"off", "on", "onto", "out", "over",
		"past", "to", "under", "with", "without"]
	
	# Randomly choose and return a preposition
	word = random.choice(words)
	return word

def get_prepositional_phrase(quantity):
	"""Build and return a prepositional phrase composed of three
	words: a preposition, a determiner, and a noun by calling the
	get_preposition, get_determiner, and get_noun functions.

	Parameter
		quantity: an integer that determines if the determiner
			and noun in the prepositional phrase returned from
			this function are single or pluaral.
	Return: a prepositional phrase.
	"""

	prepositional_phrase = ""

	if quantity == 1:
		prepositional_phrase = get_determiner(1) + " " + get_noun(1) + " " + get_preposition()
	else:
		prepositional_phrase = get_determiner(2) + " " + get_noun(2) + " " + get_preposition()
	
	return prepositional_phrase

# Execute the program
main()