def solution(A):
	n = len(A)
	stack = Stack(n)
	for c in A:
		if stack.size == 0:
			stack.push(c)
		else:
			d = stack.s[stack.size - 1]
			if c != d:
				stack.pop()
			else:
				stack.push(c)
	if stack.size == 0:
		return -1
	dominator = stack.pop()
	index, count = -1, 0
	for i in range(n):
		if dominator == A[i]:
			index = i
			count += 1
	if count > (n / 2):
		return index
	return -1

class Stack:
	def __init__(self, N=0):
		self.size = 0 
		self.s = ['0'] * N

	def push(self, x):
		self.s[self.size] = x
		self.size += 1

	def pop(self):
		self.size -= 1
		return self.s[self.size]