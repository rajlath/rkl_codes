
# -*- coding: utf-8 -*-
# @Date    : 2019-03-21 21:35:27
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
qnty = RMI()
maxs = max_val
sums = 0
for i in qnty[::-1]:
    maxs = min(maxs - 1, i)
    sums += max(maxs, 0)
print(sums)

