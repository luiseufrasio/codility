import math

def solution(K, M, A):
	n = len(A)
	if K == 1:	return sum(A)
	if K >= n:	return max(A)
	kDiv = math.floor(n / K)
	max_sum = 0
	for k in range(K):
		begin = k * kDiv
		if k < K - 1:
			end = begin + kDiv
		else:
			end = n
		max_sum = max(max_sum, sum(A[begin:end]))
	return max_sum  