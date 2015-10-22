import unittest
from random import randint
import time
		
class TestFrogRiverOne(unittest.TestCase):
	def setUp(self):
		from frog_river_one import solution
		self.solution = solution

	def test_x_one(self):
		self.assertEqual(self.solution(1, [1, 1, 1, 1, 1, 1, 1, 1]), 0)

	def test_x_two(self):
		self.assertEqual(self.solution(2, [1, 1, 1, 1, 2, 1, 1, 1]), 4)
	
	def test_x_three(self):
		self.assertEqual(self.solution(3, [1, 3, 1, 3, 2, 3, 3, 3]), 4)
		
	def test_x_four(self):
		self.assertEqual(self.solution(4, [1, 3, 1, 4, 2, 3, 4, 4]), 4)
		
	def test_x_five(self):
		self.assertEqual(self.solution(5, [1, 3, 1, 4, 2, 3, 5, 4]), 6)
		
	def test_minus_one(self):
		self.assertEqual(self.solution(3, [1, 3, 1, 3, 3, 3, 3, 3]), -1)
		self.assertEqual(self.solution(4, [1, 3, 1, 4, 3, 3, 4, 4]), -1)
		self.assertEqual(self.solution(5, [1, 3, 1, 4, 3, 3, 5, 4]), -1)
		
	def test_twenty_thousand(self):
		A = []
		N = 100000
		X = randint(1, N)
		for i in range(N):
			A.append(randint(1, X))
		time_before = time.time()	
		S = self.solution(X, A)
		time_after = time.time()
		self.assertTrue(time_after - time_before <= 1, 
		"the time difference is %d" % (time_after - time_before))
		print(time_after - time_before)

class TestPermCheck(unittest.TestCase):
	def setUp(self):
		from perm_check import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution([4, 1, 3, 2]), 1)
		self.assertEqual(self.solution([4, 1, 3]), 0)

	def test_thousands(self):
		A = []
		N = 100000
		for i in range(N):
			A.append(randint(1, 1000000000))
		time_before = time.time()	
		S = self.solution(A)
		time_after = time.time()
		self.assertTrue(time_after - time_before <= 1, 
		"the time difference is %d" % (time_after - time_before))
		print(time_after - time_before)

if __name__ == '__main__':
	unittest.main()