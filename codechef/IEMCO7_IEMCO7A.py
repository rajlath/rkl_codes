
# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 22:17:12
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
    lens = RI()
    arrs = sorted(RMI())
    ones = []
    for i in range(lens):
        if arrs[i] == 1:
            ones.append(1)
        else:
            break
    ans = arrs[i:]
    if ans[-1] == 3 and ans[-2] == 2:
        ans[-1], ans[-2] = 2, 3
    ans.extend(ones)
    print(*ans)
