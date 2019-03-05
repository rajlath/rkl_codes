
# -*- coding: utf-8 -*-
# @Date    : 2019-02-28 15:20:21
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
ans  = 0
pos, neg = 0, 0
for i in elem:
    if i != 0:
        if i > 0 : pos +=1
        else:neg += 1
if pos >=   -(-lens // 2) : ans = 1
elif neg >= -(-lens // 2) : ans = -1
print(ans)
