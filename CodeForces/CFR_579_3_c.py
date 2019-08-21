from math import gcd
from functools import reduce

lens = int(input())
gc_d = reduce(gcd, [int(x) for x in input().split()])
i = 1
cnts = 0
while i * i <= gc_d:
    if gc_d % i == 0:
        cnts += 1
        cnts += (i * i != gc_d)
    i += 1    
print(cnts)
