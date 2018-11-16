def solution(N):
    gap = 0
    flag = 0
    temp = 0
    while(N>=1):
        if flag==1:
            if N%2==0:
                gap+=1
            else:
                if gap>temp:
                    temp = gap
                gap=0
        else:
            if N%2==1:
                flag = 1
        N=N//2
    if flag ==0:
        return 0
    else:
        return temp
