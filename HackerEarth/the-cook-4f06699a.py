
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 21:27:59
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


nb_types, totals = RMI()
types = RMI()
i = 0
status = ["0"] * totals
last = []
for i, v in enumerate(types):
    if v not in last:
        last.append(v)
    else:
        if len(last) == nb_types:
            status[i-1] = "1"
            last = [v]
if last and len(last ) == nb_types:
    status[-1] = "1"
print("".join(status))

