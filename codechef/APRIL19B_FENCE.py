
# -*- coding: utf-8 -*-
# @Date    : 2019-04-06 09:56:32
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

nb_test = int(input())
for _ in range(nb_test):
    n,m,k = RMI()
    counts = {}
    count  = 0
    for i in range(k):
        x, y = RMI()
        curr = (x, y)
        counts[(x, y)] = 1
        curr_count = 4
        if counts.get((x - 1, y)):curr_count -= 2
        if counts.get((x, y - 1)):curr_count -= 2
        if counts.get((x + 1, y)):curr_count -= 2
        if counts.get((x, y + 1)):curr_count -= 2
        count += curr_count
    print(count)






