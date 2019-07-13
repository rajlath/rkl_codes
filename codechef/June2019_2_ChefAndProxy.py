
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 19:49:51
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import ceil
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
    lens = RI()
    days = RW()
    present = days.count("P")
    #needed  = ceil(lens * 0.75) - present
    #print(needed)
    more    = 0
    for i in range(2, lens - 2):
        if present / lens >= 0.75:break
        if days[i] == "A":
                if (days[i - 1] == "P" or  days[i - 2] == "P") and (days[i+1] == "P" or days[i+2] == "P"):
                        present  += 1
                        more += 1

    if present / lens >= 0.75:print(more)
    else:print(-1)














