
# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 10:31:11
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
    has, nb_round, costA, costB = RMI()
    answer = (costB * nb_round - has + 1) // ( costB - costA)
    answer = min(nb_round, answer)
    if answer < 0: answer = -1
    print(answer)