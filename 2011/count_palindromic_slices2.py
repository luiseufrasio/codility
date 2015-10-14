def solution(S):
	p = 0
	N = len(S)
	for i in range(0, N-1):
		if S[i] == S[i+1]:
			p += 1
			v = i - 1
			w = i + 2
			while v >= 0 and w <= N-1:
				if S[v] == S[w]:
					p += 1
					v -= 1
					w +=1
				else:
					break
		x = i - 1
		y = i + 1
		while x >= 0 and y <= N-1:
			if S[x] == S[y]:
				p += 1
				x -= 1
				y +=1
			else:
				break
	return p
	
if __name__ == '__main__':
    solution('acaddefg')