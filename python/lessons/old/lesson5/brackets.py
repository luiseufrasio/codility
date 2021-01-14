def solution(A):
	n = len(A)
	stack = Stack(n)
	for c in A:
		if stack.size == 0:
			stack.push(c)
		else:
			d = stack.s[stack.size - 1]
			if (c == '}' and d == '{') or (c == ']' and d == '[') or (c == ')' and d == '('):
				stack.pop()
			else:
				stack.push(c)
	if stack.size == 0:
		return 1
	return 0

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