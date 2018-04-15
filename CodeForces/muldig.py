#a(n) = if n=0 then 1 else a([n/10]) * (n mod 10 + 0^(n mod 10))
'''
4
22 73 9
45 64 6
47 55 7
2 62 4
'''
from functools import reduce
from operator import mul
def getval(n):
    if n == 0:return 1
    while n > 9:
        n = reduce(mul, (int(d) for d in str(n) if d != '0'))
    return n

for _ in range(int(input())):
    l, r, k = [int(x) for x in input().split()]
    print(sum(1 for x in range(l, r+1) if getval(x)== k))



