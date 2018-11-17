def solution(A):
    l_s = 0
    r_s = sum(A)
    diff=[]
    for i in range(len(A)-1):
        l_s += A[i]
        r_s -= A[i]
        if r_s>l_s:
            diff.append(r_s-l_s)
        else:
            diff.append(l_s-r_s)
    return min(diff)
