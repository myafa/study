def solution(X, Y, D):
    z = Y-X
    jump = z//D
    onemore = z%D
    if onemore:
        return jump+1
    else:
        return jump
