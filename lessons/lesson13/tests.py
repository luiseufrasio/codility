import unittest
from random import randint
import time

class TestMinAbsSumOfTwo(unittest.TestCase):
	def setUp(self):
		from min_abs_sum_of_two import solution, solution_n2
		self.solution = solution
		self.solution_n2 = solution_n2

	def test_zero(self):
		self.assertEqual(self.solution([0]), 0)

	def test_simple1(self):
		self.assertEqual(self.solution([1, 4, -3]), 1)

	def test_simple2(self):
		self.assertEqual(self.solution([-8, 4, 5, -10, 3]), 3)
	
	def test_simple3(self):
		self.assertEqual(self.solution([8, 5, 3, 4, 6, 8]), 6)

	def test_gen1(self):
		B = [-57, 97, -87, -9, 95, 76, 2, -62, 4, -66]
		self.assertEqual(self.solution([-57, 97, -87, -9, 95, 76, 2, -62, 4, -66]), 4)

	def test_performance(self):
		A = []
		N = 100
		for i in range(N):
			A.append(randint(-10E9, 10E9))
		self.assertEqual(self.solution(A), self.solution_n2(A))

if __name__ == '__main__':
	unittest.main()