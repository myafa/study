def solution(A):
    A.sort()
    for i in range(0, len(A)):
        if A[i]!=i+1:
            return i+1
    return len(A)+1
