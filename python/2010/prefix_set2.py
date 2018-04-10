def solution(A): 
    B = {}
    p = 0 
    n = len(A)
    for i in range(n): 
        try:
            B[A[i]] += 1
        except KeyError:
            B[A[i]] = 1 
            p = i 
    return p