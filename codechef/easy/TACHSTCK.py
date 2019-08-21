
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 14:10:58
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


nb_stick, limit = RMI()
sticks = sorted([RI() for _ in range(nb_stick)], reverse = True)
pairs = 0
pos   = 0
while pos < (nb_stick - 1):
    if sticks[pos] - sticks[pos +1] <= limit:
        pos += 2
        pairs += 1
    else:
        pos += 1
print(pairs)