def solution(A):
	N = len(A)
	B = [0] * (N + 2)
	
	for i in range(N):
		B[A[i]] = 1
	
	for j in range(1, N+2):
		if B[j] == 0:
			return j