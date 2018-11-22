# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    B = [0]*N
    max = 0
    max_temp=0
    for i in range(len(A)):
        if A[i]<=N:
            B[A[i]-1]+=1
            if B[A[i]-1]>max:
                max+=1
        elif max==max_temp:
            pass
        else:
            max_temp=max
            B=[max]*N
    return B
