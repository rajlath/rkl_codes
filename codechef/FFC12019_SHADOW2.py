
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 09:06:18
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
    lens, limits = RMI()
    values = RMI()
    max_xor = 0
    for i in range(limits):
        max_xor ^= values[i]
    curr_xor = max_xor
    for i in range(limits,lens):
        curr_xor =  (curr_xor ^ values[i - limits]) ^ values[i]
        max_xor  =  max(max_xor, curr_xor)
    print(max_xor)