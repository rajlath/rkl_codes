
# -*- coding: utf-8 -*-
# @Date    : 2019-08-23 18:38:34
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
    has, switch1, switch2 = [int(x) for x in input().split()]
    for _ in range(int(input())):
        now1, now2 = [int(x) for x in input().split()]
        if switch1 == switch2:
            if now1 == now2:
                print(["OFF","ON"][has == 1])
            else:
                print(["ON","OFF"][has == 1])
        else:
            if now1 == now2:
                print(["ON","OFF"][has == 1])
            else:
                print(["OFF","ON"][has == 1])





