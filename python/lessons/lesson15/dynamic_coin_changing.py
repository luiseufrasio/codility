import sys

def print_dp(dp, i, j):
	print('i = %d' % i)
	print('j = %d' % j)
	print(dp)

def solution(C, k):
	n = len(C)
	dp = [0] + [sys.maxsize] * k
	for i in range(1, n + 1):
		for j in range(C[i - 1], k + 1):
			dp[j] = min(dp[j - C[i - 1]] + 1, dp[j])
			print_dp(dp, i, j)
	return dp[n]

if __name__ == '__main__':
	s = solution([1,3,4], 6)