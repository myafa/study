# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    if D<=0:
        return 0
    if X-Y==0:
        return 0
    if (Y-X)%D==0:
        return (Y-X)//D
    else:
        return ((Y-X)//D)+1
