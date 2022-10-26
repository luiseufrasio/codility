# https://app.codility.com/demo/results/trainingJWBEAG-A8N/

def solution(N):
    max_bin_gap = 0
    one_open = False
    curr_bin_gap = 0
    bin_N = bin(N)[2:]
    for d in bin_N:
        if d == '0' and one_open:
            curr_bin_gap += 1
        if d == '1':
            if one_open:
                if curr_bin_gap > max_bin_gap:
                    max_bin_gap = curr_bin_gap
                curr_bin_gap = 0
            else:
                one_open = True
    return max_bin_gap
