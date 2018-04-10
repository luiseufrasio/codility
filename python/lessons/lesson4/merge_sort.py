import math

def solution(A):
	n = len(A)
	if n == 1:
		return A
	half = math.floor(n/2)
	b = solution(A[:half])
	c = solution(A[half:])
	lb = len(b)
	lc = len(c)
	j, k, i = 0, 0, -1
	while i < n - 1:
		i += 1
		if j >= lb:
			A[i] = c[k]
			k += 1
			continue
		if k >= lc:
			A[i] = b[j]
			j += 1
			continue
		if b[j] < c[k]:
			A[i] = b[j]
			j += 1
		else:
			A[i] = c[k]
			k += 1
	return A