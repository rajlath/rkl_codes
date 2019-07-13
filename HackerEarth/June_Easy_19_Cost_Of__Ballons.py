
# -*- coding: utf-8 -*-
# @Date    : 2019-06-03 20:12:15
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
    costA, costB = RMI()
    nb_students = RI()
    grp1, grp2 = [], []
    for _ in range(nb_students):
        a, b = RMI()
        grp1.append(a)
        grp2.append(b)
    sum1, sum2 = sum(grp1), sum(grp2)
    cost_incurred = max(sum1, sum2) * min(costA, costB) + min(sum1, sum2) * max(costA, costB)
    print(cost_incurred)
