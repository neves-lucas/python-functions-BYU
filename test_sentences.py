from sentences import get_determiner, get_noun, get_preposition, get_verb, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
	# 1. Test the single determiners.

	single_determiners = ["a", "one", "the"]

	# This loop will repeat the statements inside it 4 times.
	# If a loop's counting variable is not used inside the
	# body of the loop, many programmers will use underscore
	# (_) as the variable name for the counting variable.
	for _ in range(4):

		# Call the get_determiner function which
		# should return a single determiner.
		word = get_determiner(1)

		# Verify that the word returned from get_determiner
		# is one of the words in the single_determiners list.
		assert word in single_determiners

	# 2. Test the plural determiners.

	plural_determiners = ["some", "many", "the"]

	# This loop will repeat the statements inside it 4 times.
	for _ in range(4):

		# Call the get_determiner function which
		# should return a plural determiner.
		word = get_determiner(2)

		# Verify that the word returned from get_determiner
		# is one of the words in the plural_determiners list.
		assert word in plural_determiners

def test_get_noun():
	# Test the single nouns.
	single_nouns = ["bird", "boy", "car", "cat", "child",
		"dog", "girl", "man", "rabbit", "woman"]

	# This loop will repeat the statements inside it 11 times.
	# If a loop's counting variable is not used inside the
	# body of the loop, many programmers will use underscore
	# (_) as the variable name for the counting variable.
	for _ in range(11):

		# Call the get_noun function which
		# should return a single noun.
		word = get_noun(1)

		# Verify that the word returned from get_noun
		# is one of the words in the single_nouns list.
		assert word in single_nouns

	# 2. Test the plural nouns.

	plural_nouns = ["birds", "boys", "cars", "cats", "children",
		"dogs", "girls", "men", "rabbits", "women"]

	# This loop will repeat the statements inside it 11 times.
	for _ in range(11):

		# Call the get_determiner function which
		# should return a plural determiner.
		word = get_noun(2)

		# Verify that the word returned from get_noun
		# is one of the words in the plural_nouns list.
		assert word in plural_nouns

def test_get_verb():
	# Test the single verbs.
	single_verbs_past = ["drank", "ate", "grew", "laughed", "thought",
		"ran", "slept", "talked", "walked", "wrote"]
	single_verbs_present = ["drink", "eat", "grow", "laugh", "think",
		"run", "sleep", "talk", "walk", "write"]
	single_verbs_future = ["will drink", "will eat", "will grow", "will laugh",
		"will think", "will run", "will sleep", "will talk",
		"will walk", "will write"]

	# This loop will repeat the statements inside it 31 times.
	# If a loop's counting variable is not used inside the
	# body of the loop, many programmers will use underscore
	# (_) as the variable name for the counting variable.
	for _ in range(31):

		# Call the get_noun function which
		# should return a single noun.
		word = get_verb(1, ["past", "present", "future"])

		# Verify that the word returned from get_noun
		# is one of the words in the single_nouns list.
		assert word in single_verbs_past or single_verbs_present or single_verbs_future

	# 2. Test the plural verbs.

	plural_verbs_past = ["drank", "ate", "grew", "laughed", "thought",
		"ran", "slept", "talked", "walked", "wrote"]
	plural_verbs_present = ["drinks", "eats", "grows", "laughs", "thinks",
			"runs", "sleeps", "talks", "walks", "writes"] 
	plural_verbs_future = ["will drink", "will eat", "will grow", "will laugh",
		"will think", "will run", "will sleep", "will talk",
		"will walk", "will write"]

	# This loop will repeat the statements inside it 11 times.
	for _ in range(11):

		# Call the get_determiner function which
		# should return a plural determiner.
		word = get_verb(2, ["present"])

		# Verify that the word returned from get_verb
		# is one of the words in the plural_verbs_present list.
		assert word in plural_verbs_past or plural_verbs_present or plural_verbs_future

def test_get_preposition():
	# List of the preppositions
	prepositions = ["about", "above", "across", "after", "along",
		"around", "at", "before", "behind", "below",
		"beyond", "by", "despite", "except", "for",
		"from", "in", "into", "near", "of",
		"off", "on", "onto", "out", "over",
		"past", "to", "under", "with", "without"]

	for _ in range(31):

		# Call the get_preposition function which
		# should return a random preposition
		word = get_preposition()

		# Verify that the word returned from get_determiner
		# is one of the words in the plural_determiners list.
		assert word in prepositions

def test_get_prepositional_phrase():
	
	# Test single
	phrase = get_prepositional_phrase(1)
	phrase.split(" ")

	assert phrase







# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])