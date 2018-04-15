print(-10//3)
n, m, one, many = [int(a) for a in input().split()]
if n < m:
    print(one * n)
else:
    bulk, rest = divmod(n, m)
    print(min(n*one, bulk*many + rest*one, -n//m) * -many))