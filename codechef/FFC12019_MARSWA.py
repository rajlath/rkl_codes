
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 08:43:23
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
    s1, s2, t1, t2 = RMI()
    nth = RI()
    if nth in range(t1, t2+1):
        curr = s1
        for i in range(t1+1, nth+1):
            curr *= 2
    elif nth < t1:
        curr = s1
        for i in range(t1 - nth):
            curr //= 2
    else:
        curr = s2
        for i in range(t2+1, nth+1):
            curr *= 2
    print(curr)


