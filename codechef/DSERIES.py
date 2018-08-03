mod = 1000000007
for _ in range(int(input())):
    n, t = [int(x) for x in input().split()]
    ans = 1
    x = 1
    for i in range(1, n+1):
        ans = (ans * (t+1))%mod


