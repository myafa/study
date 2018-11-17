import math 
def solution(N):
    # write your code in Python 3.6
    oneEx=0
    keep =0; longest=0
    length= int((math.log(N,2)))

    for i in range(length+1):
        if N-(2**(length-i))>0:
            if oneEx:
                if longest<keep:
                    longest=keep
                keep=0
            else:
                oneEx=1
            N-= 2**(length-i)
        elif N-(2**(length-i))==0:
            if oneEx:
                if longest<keep:
                    longest=keep
            return longest
        else:
            if oneEx:
                keep+=1
                
    return longest
