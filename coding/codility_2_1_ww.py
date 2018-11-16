# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if A:
        it = K%len(A)
        temp=[]
        for i in range(it):
            temp.append(A.pop())
            #print(temp)
        for j in temp:
            A.insert(0,j)
    return A
