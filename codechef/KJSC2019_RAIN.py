
# -*- coding: utf-8 -*-
# @Date    : 2019-04-14 21:23:26
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

from itertools import accumulate
nb_test = RI()
for _ in range(nb_test):
    nb_days, nb_qry = RMI()
    collected = RMI()
    for _ in range(nb_qry):
        visited = 0
        last_visit = 0
        capacity = RI()
        current = 0
        for i in range(nb_days):
            current += collected[i]
            if current > capacity:
                visited += 1
                last_visit = i
                current = collected[i]


        print(visited, last_visit)

