
# -*- coding: utf-8 -*-
# @Date    : 2019-04-30 08:58:30
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


row, col, limit = RMI()
mats = [[0 if x =="*" else 1 for x in input()] for _ in range(row)]
ans = 0
for i in range(row):
    curr = 0
    for j in range(col):
        if mats[i][j]:
            curr += 1
            ans += curr >= limit
        else:curr = 0
for i in range(col):
    curr = 0
    for j in range(row):
        if mats[j][i]:
            curr += 1
            ans += curr >= limit
        else:curr = 0
if limit == 1:
    ans //= 2
print(ans)

