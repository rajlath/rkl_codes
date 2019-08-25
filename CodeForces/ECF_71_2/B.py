
# -*- coding: utf-8 -*-
# @Date    : 2019-08-23 11:48:32
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


rows, cols = [int(x) for x in input().split()]
matrix_a =  [[int(x) for x in input().split()] for _ in range(rows)]

matrix_b = [[0 for _ in range(cols)] for _ in range(rows)]
rets = []
for i in range(rows - 1):
    for j in range(cols - 1):
        if ( matrix_a[i][j] == 1 and matrix_a[i + 1][j] == 1 and matrix_a[i][j + 1] == 1 and matrix_a[i + 1][j + 1] == 1):
            rets.append([i + 1, j + 1])
            for x in range(2):
                for y in range(2):
                    matrix_b[i + x][j + y] = 1
                    print(matrix_b)
print(rets, matrix_a, matrix_b)
if matrix_a == matrix_b:
    print(len(rets))
    for i in rets:
        print(i[0], i[1])
else:
    print(-1)

