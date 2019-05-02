
# -*- coding: utf-8 -*-
# @Date    : 2019-03-18 17:21:55
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

LIMIT = int(10 ** 5 + 1)
odddiv= [0] * LIMIT
for i in range(1, LIMIT, 2):
    odddiv[i] += i
    for j in range(2 * i, LIMIT, i):
        odddiv[j] += i

nb_test = RI()
for _ in range(nb_test):
    l, r = RMI()
    print(sum(odddiv[l:r+1]))
