import unittest
from random import randint
import time

class TestMinMaxDivision(unittest.TestCase):
	def setUp(self):
		from min_max_div import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution(3, 5, [2, 1, 5, 1, 2, 2, 2]), 6)
		
	def test_extreme_double(self):
		self.assertEqual(self.solution(3, 5, [5, 3]), 5)

	def test_simple1(self):
		self.assertEqual(self.solution(2, 7, [4, 1, 2, 7]), 7)

if __name__ == '__main__':
	unittest.main()