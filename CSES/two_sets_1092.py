
# -*- coding: utf-8 -*-
# @Date    : 2019-07-01 19:21:06
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


n = RI()
a0 = a1 = 0
sums = (n * (n + 1)) // 2
if sums % 2 != 0:
    print("NO")
else:
    ans = [None] * (n)
    willbe = sums // 2
    for i in range(n, -1, -1):
        if i <= willbe:
            willbe -= i
            a0 += i
            a[i - 1] = 1
        else:
            a[i - 1] = 0
            a1 += i
    if a1 == a0:
        print(willbe)        
