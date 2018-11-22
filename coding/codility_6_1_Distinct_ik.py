def solution(A):
    temp = {}
    for i in A:
        if i in temp.keys():
            pass
        else:
            temp[i]=1
    return len(temp)
