def solution(S):
    # write your code in Python 3.6
    lens = len(S)
    if lens == 0: return -1
    if lens == 1: return  0
    i = 1
    while i < lens:
        left = S[0:i]
        rite = S[i+1:i+i+1][::-1]
        #print(left, rite)
        if left == rite:return i
        i += 1


print(solution("rajjar"))