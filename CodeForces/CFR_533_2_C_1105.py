mod = int(1e9 + 7)
n, l, r = [int(x) for x in input().split()]
dp = [[0 for _ in range(n+1)] for _ in range(3)]
dp[0][0] = r // 3  -  (l - 1) // 3
dp[0][1] = (r + 2) // 3 - (l + 1) // 3
dp[0][2] = (r + 1) // 3 - (l) // 3
for i in range(n):
    for  j in range(3):
        for k in range(3):
            dp[i][(i+j)%3] = ( dp[i][(j+k)%3] + dp[i-1][k]*dp[0][j] ) % mod
print(dp[n-1][0])