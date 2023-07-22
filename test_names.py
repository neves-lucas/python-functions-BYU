from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
	# Call the "Make full name" function and verify if it will display in the right order
	fname = make_full_name("Lucas", "Neves")
	assert isinstance(fname, str), "Full name must return a string"

	# Testing with parameters
	assert make_full_name("Mariana", "Dutra") == f"Dutra;Mariana"
	assert make_full_name("Mariana", "") == f";Mariana"
	assert make_full_name("", "Dutra") == f"Dutra;"
	assert make_full_name("", "") == f";"

def test_extract_family_name():
	# Call the "Extract family name" function and verify if it works properly
	fmname = extract_family_name("Neves;Lucas")
	assert isinstance(fmname, str), "Family name must return a string"

	# Testing with parameters
	assert extract_family_name("Dutra;Mariana") == "Dutra"
	assert extract_family_name("Neves;Lucas") == "Neves"

def test_extract_given_name():
	# Call the "Extract given name" function and verify if it works properly
	gname = extract_given_name("Neves;Lucas")
	assert isinstance(gname, str), "Given name must return a string"

	# Testing with parameters
	assert extract_given_name("Dutra;Mariana") == "Mariana"


pytest.main(["-v", "--tb=line", "-rN", __file__])

