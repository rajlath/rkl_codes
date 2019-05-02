
# -*- coding: utf-8 -*-
# @Date    : 2019-03-07 21:05:32
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


nb_students = RI()
strengths = sorted(RMI())
maxs = 0
last, curr  = 0, 0
while curr < nb_students:
    while curr < nb_students and strengths[curr] - strengths[last] < 6: curr += 1
    maxs = max(maxs, curr - last)
    last += 1
print(maxs)

