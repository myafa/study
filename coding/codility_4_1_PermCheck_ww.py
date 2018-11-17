def solution(A):
    check={}
    maxi = max(A)
    
    if 1 not in A or len(A) not in A:
        return 0
    elif maxi != len(A):
        return 0
    else:
        for i in range(len(A)):
            check[i]=0
        for a in A:
            check[a-1]+=1
            if check[a-1]>1:
                return 0
    return 1
