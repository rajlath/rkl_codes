
# -*- coding: utf-8 -*-
# @Date    : 2019-03-20 08:17:01
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


lens = RI()
order= RMI()
original = [0]
for o in order:
    original.append(original[-1] + o)
minorginal = min(original)
original = [o - minorginal + 1 for o in original]
if sorted(original) == list(range(1, lens + 1)):
    print(*original)
else:
    print(-1)