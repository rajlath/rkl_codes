
# -*- coding: utf-8 -*-
# @Date    : 2019-07-01 18:37:21
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

def get_nos_ways(l):
    m, n = l, l
    grid = m * n
    total= grid * (grid - 1)
    if m > 2 and n > 1:
        total -= (m - 2) * (n - 1) * 4
    if n > 2 and n > 1:
        total -= (n - 2) * (m - 1) * 4
    return total // 2



k = RI()
for i in range(1, k + 1):
    print(get_nos_ways(i))


