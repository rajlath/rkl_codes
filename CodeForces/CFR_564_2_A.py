
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 17:39:05
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


a, b, c = RMI()
if a == b and c == 0: print("0")
elif a > b + c : print("+")
elif b > a + c: print("-")
else:print("?")