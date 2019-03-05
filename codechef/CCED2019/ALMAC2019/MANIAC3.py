
# -*- coding: utf-8 -*-
# @Date    : 2019-03-04 19:31:08
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from  itertools import accumulate
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


nb_elem, nb_query = RMI()
elems = [0] + list(accumulate(RMI()))
for _ in range(nb_query):
    l1, r1, l2, r2, fact = RMI()
    p = elems[r1] - elems[l1 - 1]
    q = elems[r2] - elems[l2 - 1]
    power = pow(p, q)
    if power < 10:
        print("No", -1)
    else:
        power = (power  // 10) % 10
        if power == fact:
            print("Yes", power)
        else:
            print("No",  power)








