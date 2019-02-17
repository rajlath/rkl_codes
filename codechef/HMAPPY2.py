from fractions import gcd
from functools import reduce

def gcd_all(*nos):
        return reduce(gcd, nos)

def lcm(a, b):
        return a * b // gcd_all(a, b)

def lcm_all(*nos):
        return reduce(lcm, nos)

nb_test = int(input())
for _ in range(nb_test):
        n, a, b, k = [int(x) for x in input().split()]
        sums = n // a + n // b  - 2 * ( n // lcm_all(a, b))
        print(["Lose", "Win"][sums >= k])


