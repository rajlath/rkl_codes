def solution(N):
    NB = bin(N)[2:]
    first  = False
    iFirst = -1
    last   = False
    gaps   = []
    for i, v in enumerate(NB):
        if v is "1":
            if first:
                gaps.append(i - iFirst - 1)
                first = False
            first = not first
            iFirst = i


    return max(gaps)

print(solution(20))
