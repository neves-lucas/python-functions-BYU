from financial_organizer import option2, read_bills
from os import path
from tempfile import mktemp
import pytest

def test_read_bills():
	# Verifies that the read_bills function uses the filename parameter.
	# 1. Get a filename for a file that doesn't exist.
	# 2. Call the read_bills function with the filename.
	# 3. Verify that the open function inside the read_bills function
	#	raises a FileNotFoundError.


	filename = mktemp(dir=".", prefix="not", suffix=".csv")
	with pytest.raises(FileNotFoundError):
		read_bills(filename)
		pytest.fail("read_bills function must use its filename parameter.")

	filename = path.join(path.dirname(__file__), "paidbills.csv")
	bills_list = read_bills(filename)


	assert isinstance(bills_list, list), \
		"read_bills function must return a list:" \
		f" expected a list but found a {type(bills_list)}"

def test_option2(monkeypatch):
	# Verifies if the total of characters on the bills_date matches
	# the format (10).

	monkeypatch.setattr("builtins.input", lambda _: "07-03-2018")

	date = input("When are you paying that bill? (ex: 12-02-2022) ")

	assert len(date) == 10

pytest.main(["-v", "--tb=line", "-rN", __file__])