
# -*- coding: utf-8 -*-
# @Date    : 2019-03-12 13:34:44
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


nb_rows, nb_cols = RMI()
mat_A = [RMI() for _ in range(nb_rows)]
mat_B = [RMI() for _ in range(nb_rows)]
mat_AB= [[] for _ in range(nb_rows+nb_cols)]
mat_BA= [[] for _ in range(nb_rows+nb_cols)]
for i in range(nb_rows):
    for j in range(nb_cols):
        mat_AB[i + j].append(mat_A[i][j])
        mat_BA[i + j].append(mat_B[i][j])
#print(mat_AB)
mat_ABS = [sorted(x) for x in mat_AB]
mat_BAS = [sorted(x) for x in mat_BA]
print(["NO", "YES"][mat_ABS == mat_BAS])
