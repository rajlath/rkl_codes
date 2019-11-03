
# -*- coding: utf-8 -*-
# @Date    : 2019-08-31 09:47:54
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
    vals = RMI()
    max_last = vals[-1]
    cnts = 0
    for i in range(lens - 2, -1, -1):
        if vals[i] > max_last:
            cnts += 1
        else:
            max_last = vals[i]
    print(cnts)

