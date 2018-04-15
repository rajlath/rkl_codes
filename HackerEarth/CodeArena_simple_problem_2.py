'''
5
RRBRR

3
'''
from itertools import groupby
n = int(input())
a = groupby(x for x in input())
print(len(list(a)))
