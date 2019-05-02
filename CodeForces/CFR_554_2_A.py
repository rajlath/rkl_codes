
# -*- coding: utf-8 -*-
# @Date    : 2019-04-25 07:51:03
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

ODD = lambda y: len([x for x in y if x%2])
a, b = RMI()
ao, bo = ODD(RMI()), ODD(RMI())
print( min(ao, b - bo) + min(bo, a - ao) )
