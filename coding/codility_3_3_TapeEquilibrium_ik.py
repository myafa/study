# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    all_sum = sum(A)
    step_sum = 0
    gap_min = all_sum-2*A[0]
    m = 1
    if gap_min<0:
        m = -1
    for i in range(len(A)-1):
        step_sum +=A[i]
        c = all_sum-step_sum
        temp = step_sum-c
        if temp==0:
            return 0
        elif temp <0:
            if temp*(-1)<gap_min*m:
                gap_min=temp
                m = -1
        else:
            if temp<gap_min*m:
                gap_min=temp
                m = 1
    return gap_min*m
