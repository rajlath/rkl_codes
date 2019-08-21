
# -*- coding: utf-8 -*-
# @Date    : 2019-08-19 13:31:51
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


import bisect
from itertools import accumulate

lens, nb_query = RMI()
values = RMI()
values = list(accumulate(values))
for _ in range(nb_query):
    curr = int(input())
    curr %= values[lens - 1]
    print(1 + bisect.bisect_left(values, curr + 1) - values[0])
