
# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 08:54:46
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
strs = RW()

valids = ''
left = 0
rite = 1
while rite < lens:
  if strs[left] != strs[rite]:
    valids += strs[left] + strs[rite]
    left = rite+1
    rite += 2
  else:
    rite += 1
print(lens - len(valids))
print(valids)





