
# -*- coding: utf-8 -*-
# @Date    : 2019-03-06 19:16:50
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


nb_sweets = RI()
sizes = RMI()
pairs = [0] * (2 * 10 ** 5 + 100)
for i in range(nb_sweets):
    for j in range(nb_sweets):
        pairs[sizes[i] + sizes[j]] += 1
print(max(pairs) // 2)