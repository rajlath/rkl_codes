
# -*- coding: utf-8 -*-
# @Date    : 2019-07-12 20:23:58
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

ins = [[x for x in y] for y in input().split()]
nums = [x[0] for x in ins]
suits= [x[1] for x in ins]
if len(set(suits)) == 1 and len(set(nums)) == 1 or sum(nums)//3 == nums[1]



