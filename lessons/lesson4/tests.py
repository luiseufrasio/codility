import unittest
from random import randint
import time
		
class TestMergeSort(unittest.TestCase):
	def setUp(self):
		from merge_sort import solution
		self.solution = solution

	def test_zero(self):
		self.assertEqual(self.solution([3,2,1]), [1,2,3])
		self.assertEqual(self.solution([3,2,1,6,5,4]), [1,2,3,4,5,6])
	
	def test_performance(self):
		A = []
		N = 1000000
		for i in range(N):
			A.append(randint(0, 1000))
		time_before = time.time()	
		S = self.solution(A)
		time_after = time.time()
		
		time_before2 = time.time()	
		A.sort()
		time_after2 = time.time()

		print(time_after - time_before)
		print(time_after2 - time_before2)
		
if __name__ == '__main__':
	unittest.main()