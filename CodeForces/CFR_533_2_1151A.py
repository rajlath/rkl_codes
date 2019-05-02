
# -*- coding: utf-8 -*-
# @Date    : 2019-04-19 15:19:15
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

need = "ACTG"
lens = RI()
has  = RW()
mins = max_val
for i in range(lens - 3):
    curr_need = 0
    for j in range(4):
        curr = abs(ord(has[i + j]) - ord(need[j]))
        curr_need += min(curr, 26 - curr)
    mins = min(mins, curr_need)
print(mins)
