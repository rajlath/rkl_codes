import math
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
sa = set(a)
lsa = len(sa)
csa = [a.count(x) for x in sa]
mcsa= max(csa)
print( int(math.ceil(mcsa /  k) * lsa * k  - n) )