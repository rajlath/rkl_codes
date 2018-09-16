INF = int(1e9 + 7) * -1
n, c, s = [int(x) for x in input().split()]
a = [0] * (n+1)
b = [0] * (n+1)
for i in range(n):
    x, y = [int(x) for x in input().split()]
    a[i] = x
    b[i] = y
dp = [INF for x in range(1 << n)]
dp[0] = 0
ans   = 0
while True:
    ans += 1
    for x in range(1, 1 << n):

        for i in range(1, n):

            y = x | (1 << i)
            if y == x:continue
            if dp[x] >= a[i]:
                dp[y] = max(dp[y], dp[x]-a[i])
    for x in range(1, 1<<n):

        sums = s
        for i in range(1, n):

            if x >> (i & i) == 1:
                sums += b[i]
        dp[x] += sums
        if dp[x] >= c:
            print(ans)
            exit()







