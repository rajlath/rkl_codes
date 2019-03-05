
# -*- coding: utf-8 -*-
# @Date    : 2019-03-05 14:23:47
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


nb_house = RI()
a = [[] for _ in range(nb_house)]
houses = RMI()
for i, v in enumerate(houses):
    a[v - 1]  += i,
s = 0
x, y = 0, 0
for u, v in a:
    s += min(abs(x - u) + abs(y - v) , abs(x - v) + abs(y - u))
    x, y = u, v
print(s)