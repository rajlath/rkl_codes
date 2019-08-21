from operator import mul
from functools import reduce

def factors(n):
    return len(set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    ))

MOD = int(10e9 + 7)
lens = int(input())
arrs = [int(x) for x in input().split()]
prods = reduce(mul, arrs) % MOD
p = []
for i in range(lens):
    p.append(factors(prods//arrs[i] % MOD))
print(sum(p))
    
    