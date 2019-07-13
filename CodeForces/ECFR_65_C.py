
# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 21:46:41
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


nb_frnds, nb_groups = RMI()
groups = []
for _ in range(nb_groups):
  c,*grp = RMI()
  groups.append(grp)
print(groups)
