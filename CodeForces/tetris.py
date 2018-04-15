'''
3 9
1 1 2 2 2 3 1 2 3
'''
from collections import Counter
cols, squares = [int(x) for x in input().split()]
colsarr = [0]*cols
squarr  = Counter([int(x)-1 for x in input().split()])
if len(squarr) == cols:
    print(min(squarr.values()))
else:
    print(0)

