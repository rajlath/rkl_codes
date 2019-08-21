
# -*- coding: utf-8 -*-
# @Date    : 2019-07-21 13:28:48
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


for _ in range(int(input())):
    has = list(input())
    lens= len(has)
    could_be_1 = "+-" * (lens//2) + "+" * (lens%2)
    could_be_2 = "-+" * (lens//2) + "-" * (lens%2)
    diff1 = sum([1 for x, y in zip(has, could_be_1) if x != y])
    diff2 = sum([1 for x, y in zip(has, could_be_2) if x != y])
    print(min(diff1, diff2))
