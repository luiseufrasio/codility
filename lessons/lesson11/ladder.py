import math

def solution(A, B):
    L = max(A)
    fib = [0] * (L + 2)
    fib[1] = 1
    for i in range(2, L + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    n = len(A) 
    R = [0] * n
    for i in range(n):
        a, b = A[i] + 1, B[i]
        R[i] = fib[a] % int(math.pow(2, b))
    return R