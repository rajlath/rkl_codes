
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 09:04:09
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
    row, col = RMI()
    ans = "Stable"
    for i in range(row):
        curr = RMI()
        if ans == "Stable":
            for j in range(col):
                sides = 0
                sides += [2, 1][i == 0 or i == row - 1]
                sides += [2, 1][j == 0 or j == col - 1]
                if curr[j] >= sides:
                    ans = "Unstable"
    print(ans)


