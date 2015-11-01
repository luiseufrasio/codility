import unittest
from random import randint
import time

class TestFlags(unittest.TestCase):
	def setUp(self):
		from peaks import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution([5]), 0)

	def test_three(self):
		self.assertEqual(self.solution([1,2,3,4,3,4,1,2,3,4,6,2]), 3)

if __name__ == '__main__':
	unittest.main()