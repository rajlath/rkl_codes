
# -*- coding: utf-8 -*-
# @Date    : 2019-03-07 02:50:01
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


a, b, c, d = [int(input()) for _ in range(4)]
print([0, 1][(a == d) and  (a > 0 or c == 0 )])