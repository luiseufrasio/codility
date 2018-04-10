def solution(A):
	n = len(A)
	pairs = [Pair(0, True)] * 2 * n
	for i in range(n):
		p1 = Pair(i - A[i], True)
		j = 2 * i
		pairs[j] = p1
		p2 = Pair(i + A[i], False)
		pairs[j + 1] = p2
	pairs.sort()

	numI = 0
	c = 0
	for p in pairs:
		if p.start:
			numI += c
			if numI > 10000000:
				return -1
			c += 1
		else:
			c -= 1
	return numI

class Pair:
	def __init__(self, x=0, start=True):
		self.x = x
		self.start = start
	
	def __lt__(self, other):
		if self.x < other.x:
			return True
		if self.x == other.x and self.start and not other.start:
			return True
		return False
		
	def __gt__(self, other):
		if self.x > other.x:
			return True
		if self.x == other.x and not self.start and other.start:
			return True
		return False

	def __eq__(self, other):
		if self.x == other.x and self.start == other.start:
			return True
		return False

	def __repr__(self):
		return "%d %r" % (self.x, self.start)