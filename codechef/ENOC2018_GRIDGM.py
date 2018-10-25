
# -*- coding: utf-8 -*-
# @Date    : 2018-10-08 07:48:11
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]



nb_test = read_int()
for _ in range(nb_test):
    n, m = read_ints()
    grid = []
    for i in range(n):
        grid.append(read_ints())
    for i in range(n):
        for j in range(1, m):
            grid[i][j] += grid[i][j-1]
    for i in range(m):
        for j in range(1, n):
            grid[i][j] += grid[i-1][j]
    nb_qry = read_int()
    for _ in range(nb_qry):
        x1, y1, x2, y2 = [int(x) - 1 for x in input().split()]
        ans = grid[x2][y2]

        if x1 > 0:
            ans -= grid[x1-1][y2]
        if y1 > 0:
            ans -= grid[x2][y1 - 1]
        if x1 > 0 and y1 > 0:
            ans += grid[x1-1][y1-1]
        print(ans)





