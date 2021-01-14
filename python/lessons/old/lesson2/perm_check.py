def solution(A):
	N = len(A)
	B = [-1] * (N + 1)
	for i in range(N):
		if A[i] > N:
			return 0
		B[A[i]] = 1
	for j in range(1, N + 1):
		if B[j] == -1:
			return 0
	return 1