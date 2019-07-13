
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 16:25:24
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

def solve(i, s):
    global nb_apple, sums, maxa, apples
    if i == nb_apple:
        x = s
        y = sums - s
        if y > x:
            x, y = y, x
        maxa = min(x - y, maxa)
        return
    solve(i + 1, s)
    solve(i + 1, s + apples[i])




nb_apple = RI()
apples   = RMI()
sums     = sum(apples)
maxa     = 0
maxa = solve(0, 0)
print(maxa)
