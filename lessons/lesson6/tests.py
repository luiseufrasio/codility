import unittest
from random import randint
import time

class TestDominator(unittest.TestCase):
	def setUp(self):
		from dominator import solution
		self.solution = solution

	def test_default(self):
		self.assertIn(self.solution([3,4,3,2,3,-1,3,3]), [0,2,4,6,7])
	
	def test_minus_1(self):
		self.assertEqual(self.solution([2, 1, 1, 3, 4]), -1)
	

if __name__ == '__main__':
	unittest.main()