need = int(input())
dp = [0] * (need + 1)
dp[0] = 1
for i in range(1, need + 1):
    for j in range(max(0, i - 6), i):
        dp[i] = (dp[i] + dp[j]) % 1000000007
        j += 1
print(dp[need - 1])        
        