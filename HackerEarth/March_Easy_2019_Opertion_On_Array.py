
# -*- coding: utf-8 -*-
# @Date    : 2019-03-15 08:26:11
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


mins = inf
nb_elements = RI()
elements = RMI()
for i in elements:
    ans = 0
    for j in elements:
        ans += min(abs(i - j), j)
    mins = min(mins, ans)
print(mins)