
# -*- coding: utf-8 -*-
# @Date    : 2019-08-30 20:11:52
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
vals = RMI()
even_odd = [0,0]
for i in vals:
    even_odd[i%2] += 1
print(min(even_odd))
