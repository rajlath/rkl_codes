
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 16:53:15
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
    nb_customer, nb_flavor = RMI()
    flavor_qty = [0] + RMI()
    profit = 0
    served = []
    for i in range(nb_customer):
        favorite, costA, costB = RMI()
        if flavor_qty[favorite] > 0:
            served.append(favorite)
            flavor_qty[favorite] -= 1
            profit += costA
        else:
            served.append(-1)
            profit += costB
    extras = [[i, x] for i, x in enumerate(flavor_qty) if x > 0]
    adjust = extras[:]
    for i, v in enumerate(served):
        if v == -1:
            served[i] = extras[-1][0]
            extras[-1][1] -= 1
            if extras[-1][1] <= 0:extras.pop()
    print(profit)
    print(*served)




