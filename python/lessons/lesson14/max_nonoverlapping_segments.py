def solution(A, B):
    n = len(A)
    if n == 0:
        return 0
    last = 0
    count = 1
    for i in xrange(1, n):
        overlaps = False
        if A[i] <= B[last]:
            overlaps = True
        if not overlaps:
            count += 1
            last = i
    return count