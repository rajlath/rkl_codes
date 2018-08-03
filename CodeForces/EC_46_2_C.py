#Failed at test 6
from collections import OrderedDict
segs = {}
for i in range(int(input())):
    a, b = [int(x) for x in input().split()]
    for i in range(a, b+1):
        segs[i] = segs.get(i, 0) + 1
counts = {}
for i, v in segs.items():
    counts[v] = counts.get(v, 0) + 1
count = OrderedDict(sorted(counts.items()))
for i, v in count.items():
    print(v, end=" ")





