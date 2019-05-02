
# -*- coding: utf-8 -*-
# @Date    : 2019-03-17 07:55:22
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from itertools import accumulate
sys.setrecursionlimit(10**5+1)


inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

nb_Test = RI()
for _ in range(nb_Test):
    n, p, q = RMI()
    lst = RMI()
    have = []
    for _ in range(q):
        l, r, x = RMI()
        have.append( x * (r - l + 1))
   
    print(sum(lst) + sum(sorted(accumulate(have), reverse=True)[:p]))

