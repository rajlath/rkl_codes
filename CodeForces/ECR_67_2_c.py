
# -*- coding: utf-8 -*-
# @Date    : 2019-07-01 08:11:55
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


lens, tips = RMI()
pos = [[], []]
for i in range(tips):
    mode, *ind = RMI()
    pos[mode].append(ind)
canbe = True
maybe = [-1] * (lens - 1)
for lr in pos[1]:
    for curr in range(lr[0] - 1,lr[1] - 1):
        maybe[curr] = 0
for lr in pos[0]:
    if sum(maybe[lr[0]-1:lr[1]-1]) == 0:
        canbe = False
        break
if not canbe:print("NO")
else:
    print("YES")
    answer = [int(1e7)]
    for i in range(lens - 1):
        answer += [answer[-1] + maybe[i]]
    print(*answer)





