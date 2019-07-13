
# -*- coding: utf-8 -*-
# @Date    : 2019-07-12 20:23:58
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

ins = int(input())
mode = ins % 4
if mode == 1:print(0, 'A')
elif mode == 2:print(1, 'B')
elif mode == 3:print(2, 'A')
else:print(1, "A")




