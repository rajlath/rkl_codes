
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 08:44:01
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


nb_test = RI()
counts = 0
for _ in range(nb_test):
    x1, y1, x2, y2, x3, y3 = RMI()
    len1 = pow(x1 - x2, 2) + pow(y1 - y2, 2)
    len2 = pow(x1 - x3, 2) + pow(y1 - y3, 2)
    len3 = pow(x2 - x3, 2) + pow(y2 - y3 ,2)
    len1, len2, len3 = sorted([len1, len2, len3])
    counts += len3 == (len1 + len2)
print(counts)
