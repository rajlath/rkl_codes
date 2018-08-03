
def solution(S, P, Q):
    lens = len(S)
    allA, allC, allG, allT = [[0 for x in range(lens+1)] for y in range(4)]
    for i, v in enumerate(S):
        allA[i+1] = allA[i] + (v=="A")
        allC[i+1] = allC[i] + (v=="C")
        allG[i+1] = allG[i] + (v=="G")
        allT[i+1] = allT[i] + (v=="T")

    result = [0] * len(P)
    for i in range(len(P)):
        A_cnt = allA[Q[i]+1] - allA[P[i]]
        C_cnt = allC[Q[i]+1] - allC[P[i]]
        G_cnt = allG[Q[i]+1] - allG[P[i]]
        T_cnt = allT[Q[i]+1] - allT[P[i]]
        if   A_cnt>0:result[i] = 1
        elif C_cnt>0:result[i] = 2
        elif G_cnt>0:result[i] = 3
        else:result[i] = 4
    return result

print(solution("CAGCCTA",[2,5,0],[4,5,6]))
