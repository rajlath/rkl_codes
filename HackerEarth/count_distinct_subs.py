mod = int(10 ** 9 + 7)
def count_sub(lens, ss):
    dp = [-1 for x in range(lens)]
    l  = [-1 for _ in range(lens)]
    for i in range(1, lens+1):
        dp[i] = dp[i-1]*2 % mod
        if l[ss[i]] > 0:
            dp[i] = (dp[i] - dp[l[s[i]]]  - 1)%mod
        l[s[i]] = 1
    return dp[lens-1]

print(count_sub(4, "abcd"))


