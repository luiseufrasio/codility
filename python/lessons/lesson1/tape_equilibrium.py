def solution(A):
	N = len(A)
	S = {0: 0, }
	D = {N: 0, }
	
	i = 1
	j = N - 1
	while i <= N - 1 and j >= 1:
		S[i] = S[i-1] + A[i-1]
		D[j] = D[j+1] + A[j]
		i += 1
		j -= 1
	
	min_diff = 1000000
	for index in range(1, N):
		p = abs(S[index] - D[index])
		if p < min_diff:
			min_diff = p
	
	return min_diff