
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 22:29:13
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
    curr , _ = RMI()
    ans = 1
    lens = len(set(str(curr)))
    if lens == 3:ans = 27
    if lens == 2:ans = 9
    print(ans)
