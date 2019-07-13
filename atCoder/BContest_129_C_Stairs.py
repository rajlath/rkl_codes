mods = 1000000007
n, m = [int(x) for x in input().split()]
bads = [True] * (n + 1)
for i in range(m):
    bads[int(input())] = False
dp = [0] * (n + 1)
dp[0] = 1
for curr in range(n):
    for next in range(curr + 1, min(n, curr + 2) + 1):
        if bads[next]:
            dp[next] += dp[curr]
            dp[next] %= mods
print(dp[n])

