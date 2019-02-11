from collections import defaultdict
from collections import Counter
from itertools import groupby
n, m = [int(x) for x in input().split()]
states = defaultdict(int)
for i in range(n):
    curr = groupby([int(x) for x in input().split()])
    for k, g in curr:
        key = k
        lens = len(list(g))
        if lens >= 2:
            states[key] += lens
maxb = int(-10e18)
#print(states)
for k, v in states.items():
    if v > maxb:
        maxb = v
        key  = k
    if v == maxb:
            key = min(key, k)
            maxb = v
print(key, maxb)






