
# -*- coding: utf-8 -*-
# @Date    : 2019-03-24 13:26:16
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


n, m, g = RMI()
rains   = RMI()
time_to_dry = RMI()
buffer = [x - y for x, y in zip(rains[1:], rains[:])]
gr = 0
collected = []
done = 0
for i in buffer:
    collect = 0
    for k, v in enumerate(time_to_dry):
        if v <= i:
            collect += 1
    collected.append(collect)
print(max(collected))


