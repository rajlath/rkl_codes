
# -*- coding: utf-8 -*-
# @Date    : 2019-08-19 07:54:04
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

nb_test = RI()
for _ in range(nb_test):
    nb_coke, minute, amb_temp, left, rite = RMI()
    should_be = 10e12
    for i in range(nb_coke):
        temperature, cost = RMI()
        will_be = amb_temp
        if temperature > amb_temp + 1:
            will_be = max(temperature - minute, amb_temp)
        elif temperature < amb_temp - 1:
            will_be = min(temperature + minute, amb_temp)
        if left <= will_be <= rite:
            should_be = min(should_be, cost)
    print([should_be, -1][should_be == 10e12])






