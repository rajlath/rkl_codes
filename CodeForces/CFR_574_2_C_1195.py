
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 08:11:37
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


nb = RI()
h1 = RMI()
h2 = RMI()
r1, r2 = 0, 0
for x, y in zip(h1, h2):
    r1, r2 = max(r1, r2 + y), max(r2 , r1 + x)
print(max(r1, r2))    