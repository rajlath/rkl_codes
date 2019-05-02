
# -*- coding: utf-8 -*-
# @Date    : 2019-04-29 21:48:57
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
grid = [[x for x in input()] for _ in range(lens)]

for i in range(1, lens - 1):
    for j in range(1, lens - 1):
        if grid[i][j] == ".":
            if grid[i-1][j] == grid[i+1][j] == grid[i][j-1] == grid[i][j+1] == ".":
                grid[i][j] = "1"
                grid[i+1][j] = "1"
                grid[i-1][j] = "1"
                grid[i][j+1] = "1"
                grid[i][j-1] = "1"
ans = "YES"
for i in range(lens):
    for j in range(lens):
        if grid[i][j] == ".":
            ans = "NO"
            break
    if ans == "NO":break
print(ans)