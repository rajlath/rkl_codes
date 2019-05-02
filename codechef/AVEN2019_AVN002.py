
# -*- coding: utf-8 -*-
# @Date    : 2019-04-29 08:08:14
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from collections import Counter
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

ans = [int(int(input()) ** 0.5) for _ in range(int(input()))]
print("\n".join(map(str, ans)))