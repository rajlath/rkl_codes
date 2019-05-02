
# -*- coding: utf-8 -*-
# @Date    : 2019-03-15 21:58:07
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


nb_participant = RI()
plus_time = max_val
min_tot_time = max_val
prog_time = 0
for _ in range(nb_participant):
    cobol, pole, dough = RMI()
    curr_time = cobol + pole + dough
    prog_time += cobol
    plus_time = min(plus_time, pole + dough)
    min_tot_time = max(prog_time + plus_time,curr_time)
print(min_tot_time)

