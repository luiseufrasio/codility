def solution(A):
    n = len(A)
    diffs = 0
    A.sort()
    old = None
    for i in xrange(n):
        if old != A[i]:
            diffs += 1
            old = A[i]
    return diffs