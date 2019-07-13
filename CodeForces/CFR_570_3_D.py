
# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 10:37:07
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
    cnts = [0] * lens
    for i in vals:
        cnts[i - 1] += 1
    cnts.sort()
    maxv = cnts[-1] + 1
    answer = 0
    for i in range(lens - 1, -1, -1):
        if cnts[i] >= maxv: cnts[i] = maxv - 1
        maxv = cnts[i]
        answer += max(0, cnts[i])
    print(answer)
