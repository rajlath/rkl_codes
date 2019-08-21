import math

n, m, q = [int(x) for x in input().split()]
g = math.gcd(n, m)
ds = [None, n // g, m // g]
buf = []
for _ in range(q):
    sx, sy, ex, ey = [int(x) for x in input().split()]
    s_area = (sy - 1) // ds[sx]
    e_area = (ey - 1) // ds[ex]
    print(["NO", "YES"][s_area == e_area])
