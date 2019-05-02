
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 12:27:55
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


ans , multip = 1, 1
digits=[int(x) for x in str(RI())]
digits=digits[::-1]
for digit in digits:
    ans = max( digit * ans , digit * multip - multip, multip)
    multip *= 9
    #print(ans, multip)
print(ans)