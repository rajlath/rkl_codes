
# -*- coding: utf-8 -*-
# @Date    : 2019-05-29 16:52:46
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


details, mods = RMI()
starts = set()
ans = "Yes"
while details % mods != 0:
    current = details % mods
    if current in starts:
        ans = "No"
        break
    else :
        starts.add(current)
        details += details % mods
print(ans)

