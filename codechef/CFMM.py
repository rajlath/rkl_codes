
# -*- coding: utf-8 -*-
# @Date    : 2019-04-22 16:09:03
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from collections import Counter
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
    lens = RI()
    count_all = Counter()
    for _ in range(lens):
        count_all += Counter(RW())
    mins = max_val
    for i in set("codechef" ):
        if i in count_all:
            mins = min(mins, count_all[i] // "codechef".count(i))
        else:
            mins = 0
            break
    print(mins)


