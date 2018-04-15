'''
s =787 354 12 456 79 13 765
'''

from math import factorial
from itertools import permutations
from collections import Counter

noe = int(input())
arr = [-1 if int(x)%2 else 1 for x in input().split()]
odds = arr.count(-1)
evens= noe - odds
max_combo = min(odds, evens)

print(2 * max_combo)
'''
787 79 13
354 12 456
354 787  354 79 354 13
354 12 787 79   354 787 787 13   354 12 456 787 79 13 6
3 * 3
2 * 2 * 2 * 3
3 * 3 * 3 * 3
9 24 81
'''

