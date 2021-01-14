def solution(A):
	N = len(A)
	B = {}
	MAX_VALUE = 1
	for i in range(N):
		if A[i] >= 0:
			B[A[i]] = 1
		if A[i] > MAX_VALUE:
			MAX_VALUE = A[i]
	j = 0
	while j <= MAX_VALUE:
		j += 1
		try:
			B[j] += 1
		except KeyError:
			return j
	return MAX_VALUE + 1