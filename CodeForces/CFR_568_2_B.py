def solve(src, tgt):
    si = 0
    ti = 0
    ans = "YES"
    while si < len(src) and ti < len(tgt):
        if src[si] == tgt[ti]:
            si += 1
            ti += 1
        else:
            if ti >= 1:
                if tgt[ti] == tgt[ti-1]:
                    ti += 1
                    continue
                else:
                    ans = "NO"
                    break
            ans = "NO"
            break
    #print(si, ti)
    if si < len(src): ans = "NO"
    else:
        if ti < len(tgt):
            while ti < len(tgt):
                if tgt[ti] == tgt[ti - 1]:
                    ti +=1
                else:
                    ans = "NO"
                    break
            if ti < len(tgt):ans = "NO"
    return  ans
nb_Test = int(input())
for _ in range(nb_Test):
    src = input()
    tgt = input()
    print(solve(src, tgt))
