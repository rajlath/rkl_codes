from fractions import gcd
from functools import reduce

print(reduce(gcd, [4,8,16], 10))
