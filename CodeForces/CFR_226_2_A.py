from fractions import gcd
from functools import reduce
print(int(input()) * reduce(gcd, [int(x) for x in input().split()]))