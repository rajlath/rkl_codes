'''
def score(a, b):
    la = len(a)
    lb = len(b)
    if la == lb:
        cnt = 0
        for i in range(la):
            cnt += a[i] != b[i]
        return cnt

    ok = 0
    if la > lb:
        a, b = b, a
        ok = 1
    cnt = 0
    j = 0
    for i in range(la):
        if b[j] != a[i]:
            if cnt:
                if ok:
                    a, b = b, a
                    return 0
            cnt += 1
            j += 1
        if j == lb or b[j] != a[i]:
            if ok:
                a, b = b, a
            return 0
        j += 1
    if ok:
        a, b = b, a
    return 1
a, b = input(), input()
print(score(a, b))
'''
def DP(src, tgt, sl, tl):
    dp = [[0 for _ in range(sl+1)] for _ in range(tl+1)]
    for i in range(sl+1):
        for j in range(tl+1):
            if i == 0: dp[i][j] = j
            elif j == 0: dp[i][j] = i
            elif src[i - 1] == tgt[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(min(dp[i][j-1],dp[i-1][j]),dp[i-1][j-1])
    return dp[sl][tl]

src = input()
tgt = input()
print(DP(src, tgt, len(src), len(tgt)))

