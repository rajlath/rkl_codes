
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 19:42:56
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]



lens = RI()
ids  = RMI()
sequence = {}
best = first = 0
for i in range(n):
    if ids[i] in sequence:
        first = max(first, sequence[ids[i]] + 1)
    best = max(best, i - first + 1)
    sequence[ids[i]] = i
print(best)

input()
best=0
cur=set()
si = 0
vs=input().split()
for i in vs:
    if i in cur:
        while vs[si] != i:
            cur.remove(vs[si])
            si += 1
        si += 1
    else:
        cur.add(i)
    best=max(best, len(cur))
print(best)

