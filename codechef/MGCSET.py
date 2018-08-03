for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    arr  = [int(x) for x in input().split()]
    dp = [[ 0 for x in range(m)] for y in range(n)]
    dp[0][0] += 1
    dp[0][arr[0] % m] += 1
    print(dp)
    for i in range(1, n):
        for j in range(m):
            dp[i][j] = dp[i-1][j]
        for j in range(m):
            dp[i][(j + arr[i]) % m] += dp[i-1][j]
    print(dp[n-1][0])

