
# -*- coding: utf-8 -*-
# @Date    : 2019-08-25 17:46:47
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


given = input()
stack = ['']
cnts  = 0
for g in given:
    if g == stack[-1]:
        cnts += 1
        stack.pop()
    else:
        stack.append(g)
print(["No", "Yes"][cnts % 2])
