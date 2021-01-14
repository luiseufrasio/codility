def solution(A):
    n = len(A)
    diffs = 0
    A.sort()
    for i in xrange(n):
        j, k = i + 1, i + 2
        if j == n or k == n:
            break
        if A[i] + A[j] > A[k] and A[i] + A[k] > A[j] and A[k] + A[j] > A[i]:
            return 1
    return 0