
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

from math import ceil, floor
nb_test = RI()
for _ in range(nb_test):
    lens = RI()
    days = RW()
    #needed = ceil(lens * 0.75) -  days.count("P")
    present = days.count("P")
    #print((needed + days.count("P"))/lens)
    #print(needed)
    can_do = 0
    for i in range(2, lens - 2):
        if days[i] == "A":
            #print(i)
            if ( days[i-1] == "P" or
                 days[i-2] == "P" or
                 days[i+2] == "P" or
                 days[i+1] == "P"
               ) :
               #print(i, "ok")
               #needed -= 1
               can_do += 1
            #if needed == 0:
            #    break
    #if needed > 0:print(-1)
    #else:print(ans)

    if (can_do + present) / lens < 0.75:
        print(-1)
    else:
        for i in range(1, can_do + 1):
            if (i + present) / lens >= 0.75:
                print(i)
                break












