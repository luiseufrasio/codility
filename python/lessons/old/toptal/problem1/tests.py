import unittest
from random import randint
import time
		
class TestProbOne(unittest.TestCase):
	def setUp(self):
		from prob_one import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution(5,[5,5,1,7,2,3,5]), 4)

	def test_zero1(self):
		self.assertEqual(self.solution(5,[5]), 0)

	def test_zero2(self):
		self.assertEqual(self.solution(1,[5,5,1,7,2,3,5]), 6)

	def test_zero3(self):
		self.assertEqual(self.solution(2,[5,5,1,2,2,3,5]), 5)

	def test_zero4(self):
		self.assertEqual(self.solution(5,[5,5,5,7,2,3,5]), 3)

	def test_performance(self):
		A = []
		N = 100000
		for i in range(N):
			A.append(randint(0, 100000))
		time_before = time.time()
		X = randint(1, 100000)	
		S = self.solution(X, A)
		time_after = time.time()
		self.assertTrue(time_after - time_before <= 1, 
		"the time difference is %d" % (time_after - time_before))
		print(time_after - time_before)
		
if __name__ == '__main__':
	unittest.main()