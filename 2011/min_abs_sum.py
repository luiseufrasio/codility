def solution(A):
	A = sorted(A, key=abs, reverse=True)
	S = 0	
	for n in A:
		if abs(S + n) <= abs(S - n):
			S += n
		else:
			S -= n

	return abs(S)
if __name__ == '__main__':
    print(solution([2, 4, 6, 8]))