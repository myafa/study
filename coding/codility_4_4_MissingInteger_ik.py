def solution(A):
    # write your code in Python 3.6
    temp = {}
    for i in A:
        if i in temp.keys():
            pass
        else:
            temp[i]=1
    temp2=1
    for i in range(len(temp)):
        if temp2 in temp.keys():
            temp2+=1
        else:
            return temp2
    return temp2
