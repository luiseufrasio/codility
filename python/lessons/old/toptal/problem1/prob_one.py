def solution(X,A):
	n = len(A)
	if n == 0 or n == 1:
		return 0
	
	k = int(n / 2)
	c_before = 0
	for i in xrange(k):
		if A[i] == X:
			c_before += 1
	c_after = 0
	for i in xrange(k, n):
		if A[i] != X:
			c_after += 1
	
	while c_before != c_after:
		if c_before > c_after:
			k -= 1
			if k >= 0:
				if A[k] == X:
					c_before -= 1
				else:
					c_after += 1
			else:
				break
		if c_after > c_before:
			k += 1
			if k < n:
				if A[k] == X:
					c_before += 1
				else:
					c_after -= 1
			else:
				break
	return k