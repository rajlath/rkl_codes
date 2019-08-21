
# -*- coding: utf-8 -*-
# @Date    : 2019-08-19 07:18:35
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
    n = int(input())
    diffs = []
    score = 0
    for i in range(n):
        given = input()
        diffs.append(given[:n//2].count("1") - given[n//2:].count("1"))
    mins = sum(diffs)
    if mins == 0:
        print(0)
    else:
        print(min([abs(mins - 2 * diffs[i]) for i in range(n)]))




