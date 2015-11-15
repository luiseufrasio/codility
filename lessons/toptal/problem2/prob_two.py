def negabinary(i):
    digits = []  
    while i != 0:
        i, remainder = divmod(i, -2)
        if remainder < 0:
            i, remainder = i + 1, remainder + 2
        digits.insert(0, str(remainder))
    return ''.join(digits)

def solution(A):
	n = len(A)
	number = 0
	for i in range(n):
		number += A[i] * pow(-2, i)
	x = negabinary(-1 * number)
	m = len(x)
	X = []
	for j in range(m - 1, -1, -1):
		X.append(int(x[j]))
	print(X)
	return X