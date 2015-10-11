def solution(s):
	p = 0
	n = len(s)
	for i in range(2, n+1):
		for j in range(0, n-1):
			if j + i < n+1:
				slice = s[j:j+i]
				if slice == slice[::-1]:
					p += 1
			else:
				break
	return p;
	
if __name__ == '__main__':
    solution('aabcdef')