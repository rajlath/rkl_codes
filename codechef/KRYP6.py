
# -*- coding: utf-8 -*-
# @Date    : 2019-03-08 09:11:49
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from bisect import *
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

nb_elem = RI()
element = RMI()
sort_el = []

for i in element:
    pos = bisect_left(sort_el, i)
    if not pos:
        print(-1)
    else:
        print(sort_el[pos - 1])
    insort(sort_el, i)

