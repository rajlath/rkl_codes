
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 09:22:48
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
elem = RMI()
left = 0
rite = lens - 1
last = -1
seq  = ''
while left <= rite:
    if elem[left] > last and (elem[rite] >= elem[left] or elem[rite] <= last):
        last = elem[left]
        seq += "L"
        left += 1
    elif elem[rite]  > last and (elem[left] >= elem[rite] or elem[left] <= last):
        last = elem[rite]
        seq += "R"
        rite -= 1
    else:
        break
print(len(seq))
print(seq)


