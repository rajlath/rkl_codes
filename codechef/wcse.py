sz = 10 ** 6 + 10
f  = [0 for _ in range(sz)]
done = [False for _ in range(sz)]
dp = [[0 for _ in range(101)] for _ in range(sz+1)]

def seive():
    for i in range(2, sz):
        if not done[i]:
            for j in range(i, sz, i):
                done[j] = True
                f[j] += 1
seive()
for i in range(1, sz):
    dp[i] = dp[i-1]
    dp[i][f[i]] += 1

nb_test = int(input())
for _ in range(nb_test):
    l, r, x = [int(x) for x in input().split()]
    print(dp[r][x] - dp[l-1][x])





