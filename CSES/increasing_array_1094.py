
# -*- coding: utf-8 -*-
# @Date    : 2019-07-01 17:30:43
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
arrs = RMI()
needed = 0
for i in range(1, lens):
    curr = max(0, arrs[i-1] - arrs[i])
    arrs[i] = arrs[i] + curr
    needed += curr
    #print(arrs, needed)
print(needed)

