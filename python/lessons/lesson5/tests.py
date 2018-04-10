import unittest
from random import randint
import time

class TestBrackets(unittest.TestCase):
	def setUp(self):
		from brackets import solution
		self.solution = solution

	def test_zero(self):
		print('inicio 0')
		self.assertEqual(self.solution('([)()]'), 0)
		print('fim 0')

	def test_one(self):
		print('inicio 1')
		self.assertEqual(self.solution('{[()()]}'), 1)
		print('fim 1')

if __name__ == '__main__':
	unittest.main()