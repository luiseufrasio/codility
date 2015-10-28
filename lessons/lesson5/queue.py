class QueueC:
	def __init__(self, N=0):
		self.N = N 
		self.queue = ['0'] * N
		self.head, self.tail = 0, 0

	def push(self, x):
		self.tail = (self.tail + 1) % self.N
		self.queue[self.tail] = x
	
	def pop(self):
		self.head = (self.head + 1) % self.N
		return self.queue[self.head]
		
	def size(self):
		return (self.tail - self.head + self.N) % self.N
	
	def empty():
		return self.head == self.tail