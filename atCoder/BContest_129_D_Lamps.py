
# -*- coding: utf-8 -*-
# @Date    : 2019-06-11 12:11:30
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


h, w = RMI()
inputs = []
for i in range(h):
    inputs.append([x for x in input()])
horizental = [[1 for x  in range(w+1)] for _ in range(h+1)]
vertical   = [[1 for x  in range(h+1)] for _ in range(w+1)]
print(inputs)
for i in range(h):
    for j in range(1, w ):
        try:
            if inputs[i][j] == "#":
                horizental[i][j] = 0
                continue
        except IndexError:
            print(i, j)

        horizental[i][j] = horizental[i][j - 1] + 1

for i in range(h):
    maxs = horizental[i][w - 1]
    for j in range(w - 2, -1, -1):
        if inputs[i][j] == "#":
            maxs = 0
            continue
    maxs = max(maxs, horizental[i][j])
    horizental[i][j] = maxs

for j in range(w):
    for i in range(1, h ):
        try:
            if inputs[i][j] == "#":
                vertical[i][j] = 0
                continue
        except IndexError:
            print(i, j)
    vertical[i][j] = vertical[i - 1][j] + 1

for j in range(w)            :
    maxs = vertical[h - 1][j]
    for i in range(h-2, -1, -1):
        if inputs[i][j] == "#":
            maxs = 0
            continue
    maxs = max(maxs, vertical[i][j])
    vertical[i][j] = maxs

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(horizental[i][j] + vertical[i][j])

print(ans - 1)
