def solution(A):
    # write your code in Python 3.6
    temp = {}
    for i in A:
        if i in temp.keys():
            temp[i]+=1
        else:
            temp[i]=1
    for key in temp.keys():
        if temp[key]%2:
            result=key
    return result
