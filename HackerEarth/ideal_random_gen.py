from fractions import gcd
a, b, c = [int(x) for x in input().split()]
sa = 2 * a * b
maxs, mins = 0, 0
if a >= b:
    mins = b
    maxs = a
else:
    mins = a
    maxs = b
if c <= mins:
    oa = c * c
elif c < mins and c < maxs:
    oa = c * c - (c - mins) * (c - mins)
elif c == maxs:
    oa = c * c - (maxs - mins) * (maxs - mins)
elif c > maxs:
    oa = c * c - (c - mins) * (c - mins) - (c - mins) * (c - mins)
if c > (a + b):
    print("1/1")
else:
    gcd =  gcd(oa, sa)
    print(str(oa // gcd) +"/" + str(sa // gcd))

