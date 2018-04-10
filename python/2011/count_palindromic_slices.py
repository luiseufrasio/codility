def solution(s):
	p = 0
	n = len(s)
	for i in range(2, n+1):
		for j in range(0, n + 1 -i):
			slice = s[j:j+i]
			if slice == slice[::-1]:
				p += 1
	return p;
	
if __name__ == '__main__':
    solution('aabcdef')