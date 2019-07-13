
# -*- coding: utf-8 -*-
# @Date    : 2019-06-29 08:11:19
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


src, tgt = [int(x) for x in input()], [int(x) for x in input()]
lens, lent = len(src), len(tgt)
answ = 0
nmc  = sum([1 for x, y in zip(src[:lent], tgt) if x != y])
answ += nmc % 2 == 0
for i in range(lent, lens):
    nmc += src[i] != src[i - lent]
    answ += nmc % 2 == 0
print(answ)




