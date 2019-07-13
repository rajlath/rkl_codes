
# -*- coding: utf-8 -*-
# @Date    : 2019-05-24 11:38:20
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


colors = RMI()
y, b, r = colors
for i in range(y, 0, -1):
    if i < b:
        bb = i + 1
        if bb < r:
            br = bb + 1
            print(i + bb + br)
            break




