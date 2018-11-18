def solution(X, A):
    temp = {}
    if X==0:
        return 0
    for i in range(len(A)):
        if A[i] in temp.keys():
            temp[A[i]]+=1
        else:
            temp[A[i]]=1
        if len(temp)==X:
            return i
    return -1
