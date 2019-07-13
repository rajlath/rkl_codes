
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 16:47:39
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


lens = RI()
elem = sorted(RMI())
counts = 1
for i in range(1, lens):
    if elem[i] != elem[i-1]:counts += 1
print(counts)



