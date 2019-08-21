MOD = 1000000007
lim = 100001
t, k = map(int, input().split())
A = [0] * lim
A[:k] = [1]*k
for i in range(k, lim):
    A[i] = (A[i-1] + A[i-k]) % MOD
for i in range(1, lim):
    A[i] = (A[i-1] + A[i]) % MOD
for i in range(t):
    a, b = map(int, input().split())
    print((A[b]-A[a-1]) % MOD)
