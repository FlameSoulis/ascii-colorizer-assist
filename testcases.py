import unittest
from ascii_colorizer_lib import unique_symbols, generate_mask
from main import validate_param

class TestColorizerAssist(unittest.TestCase):
	def test_unique_symbols(self):
		test = "1234567890"
		results = unique_symbols(test)
		assert len(results) == 10
		assert results == ["1","2","3","4","5","6","7","8","9","0"]

	def test_unique_symbols02(self):
		test = "   \n   abcd  \n   "
		results = unique_symbols(test)
		assert len(results) == 4
		assert results == ["a", "b", "c", "d"]
	def test_generate_mask(self):
		test = "   \n   abcd  \n   "
		results = generate_mask(test)
		assert results== "   \n   0000  \n   "
	def test_generate_mask02(self):
		test = "   \n   abcd  \n   "
		results = generate_mask(test, True)
		assert results== "   \n   1234  \n   "
	def test_validate_param(self):
		assert validate_param("-m") == 0b0100
		assert validate_param("-n") == 0b0001
		assert validate_param("-o") == 0b0010
		assert validate_param("-no") == 0b0011

if __name__ == "__main__":
    unittest.main()