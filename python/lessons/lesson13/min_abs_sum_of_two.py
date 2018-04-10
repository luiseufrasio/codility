def solution_n2(A):
	A.sort()
	min_abs = A[-1]
	n = len(A)
	for i in range(n):
		for j in range(i, n):
			min_abs = min(min_abs, abs(A[i] + A[j]))
	return min_abs

def solution(A):
	A.sort()
	if A[0] >= 0:	return 2 * A[0]
	if A[-1] <= 0:	return abs(2 * A[-1])
	min_abs = A[-1] + A[-1]
	j, k = 0, len(A) - 1
	while j <= k:
		s_abs = abs(A[k] + A[j])
		if s_abs < min_abs:	min_abs = s_abs
		if abs(A[j+1] + A[k]) <= s_abs:
			j += 1
		elif abs(A[j] + A[k-1]) <= s_abs:
			k -= 1
		else:	
			j += 1
			k -= 1
	return min_abs