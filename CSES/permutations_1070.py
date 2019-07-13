
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 09:34:05
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


n = RI()
if n == 1: print("1")
elif n < 4: print("NO SOLUTION")
elif n == 4:print("3 1 4 2")
else:
    for i in range(1, n + 1, 2):
        print(i, end = " ")
    for i in range(2, n + 1, 2)    :
        print(i, end = " ")


