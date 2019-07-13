
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 11:25:57
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


from math import floor, log2

nb_test = RI()
for _ in range(nb_test):
    current = RI()
    if current % 2 == 0:
        print("Alas")
    else:
        print(floor(log2(current)), current // 2)

