def solution(X, A):
	N = len(A)
	B = [-1] * (X + 1)
	for i in range(N):
		j = A[i]
		if B[j] == -1:
			B[j] = i
	
	max_time = 0
	for x in range(1, X + 1):
		if B[x] == -1:
			return -1
		if B[x] > max_time:
			max_time = B[x]  
	
	return max_time