a, b, c, n = [int(x) for x in input().split()]
passed   = (a - c) + (b - c) +  c
if n < (passed + 1): print(-1)
else: print(n - passed)


