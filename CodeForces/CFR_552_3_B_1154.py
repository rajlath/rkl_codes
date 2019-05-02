
# -*- coding: utf-8 -*-
# @Date    : 2019-04-16 20:29:43
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


nb = RI()
arr = RMI()
a, b= max(arr), min(arr)
if (a - b) % 2 == 0:
    diff = (a - b) // 2
    valid= [a, b, a - diff]
else:
    diff = a - b
    valid= [a, b]
for i in arr:
    if i not in valid:
        diff = -1
        break
print(diff)
