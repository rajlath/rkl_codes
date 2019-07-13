
# -*- coding: utf-8 -*-
# @Date    : 2019-06-29 09:09:37
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
import math
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


nums = RI()
flts, cels = [], []
ceil_sum = 0
for _ in range(nums):
    current = float(input())
    flts.append(current)
    cciel = math.ceil(current)
    cels.append(cciel)
    ceil_sum += cciel

sums = 0
for i in range(nums):
    if abs(flts[i] - cels[i]) > 0:
        cels[i] = math.floor(flts[i])
        sums += 1
        if sums == ceil_sum:break
for i in cels:print(i)


