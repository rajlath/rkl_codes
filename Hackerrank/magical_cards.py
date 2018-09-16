from itertools import permutations, combinations
from math import factorial
'''
def factors(n):
    gaps = [1,2,2,4,2,4,2,4,6,2,6]
    length, cycle = 11, 3
    f, fs, nxt = 2, [], 0
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += gaps[nxt]
        nxt += 1
        if nxt == length:
            nxt = cycle
    if n > 1: fs.append(n)
    return fs
'''
import math
import itertools

def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i


n = int(input())
for _ in range(n):
    a = int(input())
    pf = list(prime_factors(a))
    ans = set(permutations(pf))
    print(len(ans))




