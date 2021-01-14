def negabinary(i):
    digits = []  
    while i != 0:
        i, remainder = divmod(i, -2)
        if remainder < 0:
            i, remainder = i + 1, remainder + 2
        digits.append(remainder)
    return digits

def solution(A):
	n = len(A)
	number = 0
	for i in range(n):
		number += A[i] * pow(-2, i)
	return negabinary(-1 * number)