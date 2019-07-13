
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 17:11:12
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


nb_child, max_wt = RMI()
weight = sorted(RMI())
i = 0
j = nb_child - 1
grandula = 0

while i <= j:
    if weight[j] + weight[i] > max_wt: j -= 1
    else:
        i += 1
        j -= 1
    grandula += 1

print(grandula)





