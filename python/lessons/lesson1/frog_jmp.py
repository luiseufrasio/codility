import math

def solution(X, Y, D):
	return int(math.ceil(((Y-X) / float(D))))
	
if __name__ == '__main__':
	print(solution(10,85,30))