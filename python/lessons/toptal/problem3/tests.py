import unittest
from random import randint
import time
		
class TestProbThree(unittest.TestCase):
	def setUp(self):
		from prob_three import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution([]), 5)
		
	def test_performance(self):
		A = []
		N = 100000
		for i in range(N):
			A.append(randint(0, 1))
		time_before = time.time()	
		S = self.solution(A)
		time_after = time.time()
		self.assertTrue(time_after - time_before <= 1, 
		"the time difference is %d" % (time_after - time_before))
		print(time_after - time_before)
		
if __name__ == '__main__':
	unittest.main()