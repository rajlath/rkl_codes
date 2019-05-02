
# -*- coding: utf-8 -*-
# @Date    : 2019-03-23 09:05:42
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
pages = RMI()
days  = 0
need  = 1
for i, v in enumerate(pages):
    need = max(need, v)
    days += need == (i + 1)
print(days)


