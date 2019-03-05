def get_subset(arr, n, sums):
    dp = [False for _ in range(n)]
    for i in range(n):
        dp[i] = [False for _ in range(sums + 1)]
        dp[i][0] = True
    if arr[0] <= sums:
        dp[0][arr[0]] = True
    for i in range(1, n):
        for j in range(sums + 1):
            if arr[i] <= j:
                dp[i][j] =  dp[i-1][j] or dp[i-1][j - arr[i]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n-2][sums])            