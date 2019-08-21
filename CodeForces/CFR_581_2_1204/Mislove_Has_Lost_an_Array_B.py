
# -*- coding: utf-8 -*-
# @Date    : 2019-08-21 13:05:50
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


given, left, rite = RMI()
mins = 2 ** left - 1 + (given - left) * 1
maxs = 2 ** rite - 1 + (given - rite) * ( 2 ** (rite - 1))
print(mins, maxs)

# solution 2
given, left, rite = RMI()
mins = [1]
for i in range(2, left+1):
    mins.append(mins[-1] * 2)
for i in range(left+1, given+1):
    mins.append(1)
maxs = [1]
for i in range(2, rite+1):
    maxs.append(maxs[-1] * 2)
for i in range(rite + 1, given + 1)    :
    maxs.append(maxs[-1])
print(sum(mins), sum(maxs))

