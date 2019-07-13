
# -*- coding: utf-8 -*-
# @Date    : 2019-06-10 16:40:03
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


r, c = RMI()
grid = []
for i in range(r):
    curr_row = RMI()
    grid.append(curr_row)
    if 1 in curr_row:
        sr, sc = i, curr_row.index(1)
    if 2 in curr_row:
        dr, dc = i, curr_row.index(2)
ans = abs(sr - dr) + abs(sc - dc)
print(ans)