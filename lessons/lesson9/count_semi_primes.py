def arrayF(n):
    F = [0] * (n + 1)
    i = 2
    while (i * i <= n):
        if (F[i] == 0):
            k = i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i
                k += i
        i += 1
    return F

def solution(N, P, Q):
    F = arrayF(N)
    semi_primes = [0] * (N + 1)
    p_semi_primes = [0] * (N + 1)
    for x in xrange(4, N + 1):
        prime_factors = []
        y = x
        while F[x] > 0:
            prime_factors.append(F[x])
            x /= F[x]
        prime_factors.append(x)
        if len(prime_factors) == 2:
            semi_primes[y] = 1
        p_semi_primes[y] = p_semi_primes[y-1] + semi_primes[y]
    M = len(P)
    R = [0] * M
    for i in xrange(M):
        m, n = P[i], Q[i]
        R[i] = p_semi_primes[n] - p_semi_primes[m] + semi_primes[m]
    return R