def solution(A):
    n = len(A)
    i, j = 0, n-1
    begin, end = i, j
    max_diff = 0
    while i <= j:
        new_i = A[end] - A[i]
        new_j = A[j] - A[begin]
        new_all = A[j] - A[i]
        
        max_diff = max(max_diff, new_i, new_j, new_all)
        
        if max_diff == new_all:
            begin, end = i, j
        elif max_diff == new_i:
            begin = i
        elif max_diff == new_j:
            end = j
        i += 1
        j -= 1
        
    begin, end = 0, n-1
    while j >= begin and i <= end:
        new_i = A[end] - A[i]
        new_j = A[j] - A[begin]
        max_diff = max(max_diff, new_i, new_j)
        
        if max_diff == new_i:
            begin = i
        elif max_diff == new_j:
            end = j
        i += 1
        j -= 1
    return max_diff