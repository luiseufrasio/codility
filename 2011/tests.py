import unittest
from count_palindromic_slices import solution

class TestCountPalindromicSlices(unittest.TestCase):
	def test_zero(self):
		self.assertEqual(solution('abcdefg'), 0)
		
	def test_one(self):
		self.assertEqual(solution('aacdefg'), 1)
		self.assertEqual(solution('accdefg'), 1)
		self.assertEqual(solution('acdefgg'), 1)
		
	def test_two(self):
		self.assertEqual(solution('aaccdefg'), 2)
		self.assertEqual(solution('accdefgg'), 2)
		self.assertEqual(solution('acaddefg'), 2)
		
if __name__ == '__main__':
	unittest.main()