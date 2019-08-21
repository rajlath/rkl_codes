
# -*- coding: utf-8 -*-
# @Date    : 2019-07-21 19:46:02
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

for _ in range(int(input())):
    chgpermin, minutes, nb_plans = [float(x) for x in input().split()]
    present_cost = chgpermin * minutes
    maybe = 0
    for i in range(int(nb_plans)):
        months, calling_rate, activation_cost = [float(x) for x in input().split()]
        act_cost = activation_cost / months
        call_chg = minutes * calling_rate
        total_cost = call_chg + act_cost
        if total_cost < present_cost:
            present_cost = total_cost
            maybe = i + 1

    print(maybe)



