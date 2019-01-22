#unsolved
INF = 1 << 60
n, k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
dp = [0]
for i, t in enumerate(h):
    j = max(0, i - k)
    for v, w in zip(dp[j:i],h[j:i]):
        print(t, v, w)
