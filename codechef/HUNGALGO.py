
# -*- coding: utf-8 -*-
# @Date    : 2019-04-22 16:30:51
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
    dim = RI()
    valid = 0
    columns = []
    for _ in range(dim):
        curr_row = RMI()
        columns.extend([i for i, v in enumerate(curr_row) if v == 0])
        if 0 in curr_row:
            valid += 1
    ans = "NO"
    if valid == dim and len(set(columns)) == dim:ans = "YES"
    print(ans)

