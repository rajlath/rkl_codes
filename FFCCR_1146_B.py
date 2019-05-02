
# -*- coding: utf-8 -*-
# @Date    : 2019-04-21 15:06:27
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


ins = RW()
a_cnt = ins.count("a")
len2  = (len(ins) - a_cnt) // 2
len1  = len(ins)  - len2
if ins[:len1].replace('a', '') == ins[len1:]:
    print(ins[:len1])
else:
    print(":(")
