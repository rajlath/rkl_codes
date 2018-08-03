#http://codeforces.com/contest/992/problem/B
from math import gcd
l, r, x, y = [int(x) for x in input().split()]
if y%x != 0:print("0")
else:

    n  = y // x
    d = 1
    cnt = 0
    while d*d <= n:
        if n % d == 0:
            c = n // d
            if l<=c*x<=r and l<=d*x<r and gcd(c, d) == 1 :
                if d * d == n : cnt += 1
                else:cnt += 2

        d += 1
    print(cnt)