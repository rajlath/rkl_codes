
# -*- coding: utf-8 -*-
# @Date    : 2019-04-30 13:21:32
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


rows, cols = RMI()
grid = [[x for x in input()] for _ in range(rows)]
need = "saba"

found = 0
for i in range(rows):
        for j in range(cols):
                if grid[i][j] == "s":
                        #check rows using cols
                        if j + 3 <= cols:
                                curr = ''
                                for x in range(j, j + 4):
                                        curr += grid[i][x]
                                if curr == 'saba'        :found += 1
                        if j - 3 >= 0:
                                curr = ''
                                for x in range(j - 3, j + 1):
                                        curr = grid[i][x] + curr
                                if curr == 'sabe':found += 1
                        if i + 3 < rows:
                                curr = ''
                                for x in range(i, i + 4):
                                        curr += grid[x][j]
                                if curr == 'saba':found += 1
                        if i - 3 >= 0:
                                curr = ''
                                for x in range(i - 3, i + 1):
                                        curr = grid[x][j] + curr
                                if curr == 'saba':found += 1
                        









