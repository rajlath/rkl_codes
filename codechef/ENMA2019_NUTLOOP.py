
# -*- coding: utf-8 -*-
# @Date    : 2019-03-30 15:20:07
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
    lens = RI()
    digs = [(x, y) for  x, y in zip(input(). split(), input().split())]
    for i in digs:
        if int(i[0]) > int(i[1]):
            print(i[0] + i[1], end = ' ')
        else:
            print(i[1] + i[0], end = ' ')

