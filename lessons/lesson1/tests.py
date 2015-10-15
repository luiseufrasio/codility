import unittest
from random import randint
import time
		
class TestTapeEquilibrium(unittest.TestCase):
	def setUp(self):
		from tape_equilibrium import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution([3,1,2,4,3]), 1)
		
	def test_two_elements(self):
		self.assertEqual(self.solution([-1000, 1000]), 2000)
		
	def test_twenty_thousand(self):
		A = []
		for i in range(100001):
			A.append(randint(-1000,1000))
		time_before = time.time()	
		S = self.solution(A)
		time_after = time.time()
		self.assertTrue(time_after - time_before <= 1, 
		"the time difference is %d" % (time_after - time_before))
		print(time_after - time_before)
		
if __name__ == '__main__':
	unittest.main()