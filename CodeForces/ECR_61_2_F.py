nb = int(input())
st = input()
dp = [[-1 for _ in range(nb + 1)] for _ in range(nb + 1)]
def calc(l, r):
    res = dp[l][r]
    if res != -1: return res
    if l > r : return 0
    if l == r: return 1
    res = 1 + calc(l + 1, r)
    for i in range(l + 1, r + 1):
        if st[i] == st[l]:
            res = min(res, calc(l + 1, i - 1) + calc(i, r))
    dp[l][r] = res
    return res
print(calc(0, nb - 1))