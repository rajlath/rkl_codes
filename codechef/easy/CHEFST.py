
# -*- coding: utf-8 -*-
# @Date    : 2019-07-21 20:21:30
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


for  _ in range(int(input())):
    one, two, m = [int(x) for x in input().split()]
    mins, maxs = min(one, two), max(one, two)
    limit = m * (m + 1) // 2
    if limit <= mins:
        print(one + two  - 2 * limit)
    else:
        print(maxs - mins)