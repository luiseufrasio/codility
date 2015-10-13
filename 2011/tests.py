import unittest
from random import randint
import time

class TestCountPalindromicSlices(unittest.TestCase):
	def setUp(self):
		from count_palindromic_slices import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution('abcdefg'), 0)
		
	def test_one(self):
		self.assertEqual(self.solution('aacdefg'), 1)
		self.assertEqual(self.solution('accdefg'), 1)
		self.assertEqual(self.solution('acdefgg'), 1)
		
	def test_two(self):
		self.assertEqual(self.solution('aaccdefg'), 2)
		self.assertEqual(self.solution('accdefgg'), 2)
		self.assertEqual(self.solution('acaddefg'), 2)
		
class TestMinAbsSum(unittest.TestCase):
	def setUp(self):
		from min_abs_sum import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution([]), 0)
	
	def test_one(self):
		self.assertEqual(self.solution([-1]), 1)
		
	def test_four(self):
		self.assertEqual(self.solution([-1, 4, -5, 9]), 1)
		
	def test_five(self):
		self.assertEqual(self.solution([3, 3, 3, 4, 5]), 0)
		
	def test_twenty_thousand(self):
		A = []
		for i in range(20001):
			A.append(randint(-100,100))
		time_before = time.time()	
		S = self.solution(A)
		time_after = time.time()
		self.assertTrue(time_after - time_before <= 5, 
		"the time difference is %d" % (time_after - time_before))
		print(time_after - time_before)
		
if __name__ == '__main__':
	unittest.main()