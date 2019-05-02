
# -*- coding: utf-8 -*-
# @Date    : 2019-03-08 21:19:07
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


nb_test = RI()
for _ in range(nb_test):
    nb_days = int(input())
    schedule= list(input())
    studied = 0
    leisure = 0
    changed = 0
    for i, v  in enumerate(schedule):
        if v == "0":
            leisure += 1
            if leisure > studied:
                schedule[i] = "1"
                studied += 1
                leisure -= 1
                changed += 1
        else:
            studied += 1
    print(changed)
