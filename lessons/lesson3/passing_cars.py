def solution(A):
	n = len(A)
	P = [0] * (n + 1)
	for k in range(1, n + 1):
		P[k] = P[k - 1] + A[k - 1]
	q = 0
	for i in range(n):
		if A[i] == 0:
			q += P[n] - P[i + 1]
		if q > 1000000000:
			return -1
	return q