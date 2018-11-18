def solution(A, K):
    B=[]
    leeng = len(A)
    if leeng==0:
        return A
    K = K%leeng
    for i in range(0, leeng):
        B.append(A[i])
    
    print([A,B])
    for i in range(0, leeng):
        A[i] = B[(i+(leeng-K))%leeng]
    return A
