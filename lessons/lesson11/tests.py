import unittest
from random import randint
import time

class TestLadder(unittest.TestCase):
	def setUp(self):
		from ladder import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution([4,4,5,5,1],[3,2,4,3,1]), [5,1,8,0,1])

if __name__ == '__main__':
	unittest.main()