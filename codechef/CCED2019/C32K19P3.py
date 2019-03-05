
# -*- coding: utf-8 -*-
# @Date    : 2019-02-28 11:30:15
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
import heapq
from collections import Counter
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

s = RW()
counter = dict(Counter(s))

l = counter.keys()
l=sorted(l,key = lambda x:counter[x])
print(l)

H = []
for i in counter:
    heapq.heappush(H, (counter[i], ord(i), i))
child = {}
while len(H) > 1:
    first = heapq.heappop(H)
    secon = heapq.heappop(H)
    fc = first[2]
    sc = first[2]
    child[fc + sc] = [fc, sc]
    heapq.heappush(H,(first[0]+secon[0],first[1]+secon[1],first[2]+secon[2]))

root = max(child, key = len)

code = {}
def dfs(root, cur = ''):
    if len(root) == 1:
        code[root] = cur
    else:
        dfs(child[root][0], cur + "0")
        dfs(child[root][1], cur + "1")
dfs(root)

print("".join(code[i]))

