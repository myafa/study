def solution(A):
    l = len(A)

#    sum으로 성능조절
#    s = sum(A)
#    if s!=(l+1)*l/2:
#        return 0

    A.sort()
    for i in range(l):
        if A[i]!=i+1:
            return 0
    return 1
