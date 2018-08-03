from collections import Counter
def solution(k, C, D):
    #count number of cleaned matching pairs
    pairs = 0
    unpaired_clean = []
    for c in C:
        if c in unpaired_clean:
            pairs += 1
            unpaired_clean.remove(c)
        else:
            unpaired_clean.append(c)
    #group same colored dirty socks

    Dc = Counter(D)
    for i in unpaired_clean:
        if Dc[i] > 0:
            Dc[i] -= 1
            pairs += 1
            k -= 1
            if k == 0:return pairs

    for i, v in Dc.items():
        if Dc[i] > 2:
            socks = min(Dc[i]//2, k//2)
            k -= socks * 2
            pairs += 1
        if k <= 1: return pairs
    return pairs




print(solution(2, [1, 2, 1, 1] ,[1, 4, 3, 2, 4]))