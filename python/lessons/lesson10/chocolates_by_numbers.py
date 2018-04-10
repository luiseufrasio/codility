def solution(N, M):
    res = 1
    while N != M:
        if N % 2 == 0 and M % 2 == 0:
            N /= 2
            M /= 2
            res *= 2
        elif N % 2 == 0:
            N /= 2
        elif M % 2 == 0:
            M /= 2
        elif N > M:
            N -= M
        else:
            M -= N
    return res * N