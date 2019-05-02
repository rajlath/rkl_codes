
# -*- coding: utf-8 -*-
# @Date    : 2019-03-23 20:48:32
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from functools import reduce
import math
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


nb_elements = RI()
for _ in range(nb_elements):
    ranges      = RI()
    ans = "NO"
    sums  =  (ranges * (ranges + 1)) // 2
    fact_indx  = 2
    fact = 2
    while fact < sums:
        fact *=  (fact_indx + 1)
    print(fact)
    while fact % sums != 0 or fact_indx < ranges:
        fact *= (fact_indx + 1)
        if fact % sums == 0:
            ans = "YES"
            break
    print(ans)


