
# -*- coding: utf-8 -*-
# @Date    : 2019-03-17 15:51:42
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


nb_stack, max_height = RMI()
current = RMI()
command = RMI()
curr_pos= 0
holding = False
Finals  = current[:]
for i in command:
    if i == 1 and curr_pos > 0:
        curr_pos -= 1
    if i == 2 and curr_pos < nb_stack - 1:
        curr_pos += 1
    if i == 3:
        if not holding and Finals[curr_pos] > 0:
            Finals[curr_pos] -= 1
            holding = True
    if i == 4:
        if holding and Finals[curr_pos] < max_height:
            Finals[curr_pos] += 1
            holding = False
print(*Finals)