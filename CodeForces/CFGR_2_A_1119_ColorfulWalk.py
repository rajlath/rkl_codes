
# -*- coding: utf-8 -*-
# @Date    : 2019-04-07 13:44:03
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
colors = RMI()
right_match = lens - 1
left_match   = 0
while colors[0] == colors[right_match] == colors[left_match]:
    left_match += 1
    right_match-= 1
print(right_match)
