def solution(A):
    A.sort()
    l = len(A)
    if l==1:
        return A[0]
    else:
        for i in range(1,l-2):
            if A[i-1]==A[i]:
                pass
            elif A[i]==A[i+1]:
                pass
            else:
                return A[i]
    if A[0]!=A[1]:
        return A[0]
    else:
        return A[l-1]
        
#왜 
