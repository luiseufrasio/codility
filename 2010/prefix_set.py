# PrefixSet

def solution(A): 
    B = [] 
    p = 0 
    for i in range(0,len(A)): 
        if not A[i] in B: 
            B.append(A[i]) 
            p = i 
    return p