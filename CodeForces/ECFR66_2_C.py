
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 09:38:34
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
for _ in range(nb_test):
    lens, k = RMI()
    arrs = sorted(RMI())
    ans  = arrs[0]
    max_diff = arrs[-1] - arrs[0]
    for i in range(lens - k):
        curr = arrs[i+k] - arrs[i]
        if curr <= max_diff:
            max_diff = curr
            ans = (arrs[i + k] + arrs[i]) // 2
    print(ans)

