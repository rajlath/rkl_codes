
# -*- coding: utf-8 -*-
# @Date    : 2019-07-01 17:01:08
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


upto = RI()
given= RMI()
should_be_sum = (upto * (upto + 1)) // 2
given_sum = sum(given)
print(should_be_sum - given_sum)