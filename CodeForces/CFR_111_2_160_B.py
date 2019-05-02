
# -*- coding: utf-8 -*-
# @Date    : 2019-03-21 14:14:43
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
numb = RW()
rite = sorted([int(x) for x in numb[lens:]])
left = sorted([int(x) for x in numb[:lens]])
if all(left[i] < rite[i] for i in range(lens)) or all(left[i] > rite[i] for i in range(lens)):
    print("YES")
else:
    print("NO")
