# https://app.codility.com/demo/results/trainingJWBEAG-A8N/

def solution(N):
    max_binary_gap = 0
    one_open = False
    current_binary_gap = 0
    binary_number = bin(N)[2:]
    for digit in binary_number:
        if digit == '0' and one_open:
            current_binary_gap += 1
        if digit == '1':
            if one_open:
                if current_binary_gap > max_binary_gap:
                    max_binary_gap = current_binary_gap
                current_binary_gap = 0
            else:
                one_open = True
    return max_binary_gap
