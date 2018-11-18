def solution(A):
    A.sort()
    temp=1
    for i in A:
        if i>0:
            if temp==i:
                temp+=1
            elif temp==i+1:
                pass
            else:
                return temp
    return temp          
