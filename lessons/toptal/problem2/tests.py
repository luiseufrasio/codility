import unittest
from random import randint
import time
		
class TestProbTwo(unittest.TestCase):
	def setUp(self):
		from prob_two import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution([1,0,0,1,1]), [1,1,0,1])
		
	def test_one(self):
		self.assertEqual(self.solution([1,0,0,1,1,1]), [1,1,0,1,0,1,1])
		
if __name__ == '__main__':
	unittest.main()