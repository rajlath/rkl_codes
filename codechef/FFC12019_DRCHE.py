
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 11:34:49
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


from collections import Counter

nb_test = RI()
for _ in range(nb_test):
    lens = RI()
    arrs = dict(Counter(RMI()))
    cherry = 0
    hazardous = 0
    turn = 1
    while arrs:
        current = max(arrs)
        if arrs[current] == 1:
            cherry += current
            if current // 2 != 0:
                arrs[current] = arrs.get(current, 0) + 1
        arrs.pop(current)
        if not arrs:break
        current = max(arrs)
        if arrs[current] == 1:
            hazardous += current
            if current // 2 != 0:
                arrs[current] = arrs.get(current, 0) + 1
        arrs.pop(current)
    if cherry > hazardous:
        print("Cherry", cherry - hazardous)
    else:
        print("Hazardous")