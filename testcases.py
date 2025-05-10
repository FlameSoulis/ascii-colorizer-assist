import unittest
from ascii_colorizer_lib import unique_symbols, generate_mask

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

if __name__ == "__main__":
    unittest.main()