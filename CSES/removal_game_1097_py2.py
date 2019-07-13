n = int(raw_input())
scores   = [0] + [int(x) for x in raw_input().split()]
'''
a = [[0 for x in range(5001)] for x in range(5001)]
b = [[0 for x in range(5001)] for x in range(5001)]
for i in range(len(scores)):
	a[0][i] = scores[i]

for i in range(1, n):
	for j in range(n - 1):
		t = a[0][j] + a[i - 1][j + 1] + b[i - 1][j + 1]
		a[i][j] = max(a[0][j] + b[i - 1][j + 1], a[0][j + i] + b[i - 1][j])
		b[i][j] = t - a[i][j]
print(a[n - 1][0])
'''
cum_sum = [0] * (n + 1)
for i in range(1, n+1):
	cum_sum[i] = cum_sum[i - 1] + scores[i]
dp = [0] * n
for i in range(n - 1, -1, -1):
	dp[i] = cum_sum[i + 1] - cum_sum[i]
	for j in range(i + 1, n):
		dp[j] = cum_sum[j + 1] - cum_sum[i] - min(dp[j - 1], dp[j])
print dp[n - 1]
