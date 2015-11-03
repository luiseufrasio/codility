import math

def solution(A):
    n = len(A)
    peaks = [0] * n
    for i in range(1, n-1):
        if A[i] > max(A[i-1], A[i+1]):
            peaks[i] = 1
    k = math.floor(n / 2)
    while k > 0:
        if n % k == 0:
            y = int(n / k)
            ok = True
            for j in range(0, n - y + 1, y):
                begin = j
                end = (j + y)
                if sum(peaks[begin:end]) == 0:
                    ok = False
                    break
            if ok:
                return int(k)
        k -= 1
    return 0