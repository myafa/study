def solution(A):
    s = sum(A)
    l = len(A)
    temp_sum = 0
    pair = 0
    if s > 1000000000:
        return -1
    for i in range(l):
        if pair > 1000000000:
            return -1
        if A[i]==0:
            pair += s-temp_sum
        else:
            temp_sum += 1
    return pair
