
# -*- coding: utf-8 -*-
# @Date    : 2019-03-13 21:53:12
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
    nb_customers = RI()
    times = []
    for _ in range(nb_customers):
        a, b = RMI()
        times.append([a, b])
    #times = sorted(times, key = lambda x: x[0])
    times = sorted(times, key = lambda x: (x[0], x[1]))
    if len(times) == 1:
        print(2)
    else:
        last  = times[1]
        cnt = 0
        for i in times[1:]:
            if i[0] > last[1]:
                cnt += 1
            elif i[1] > last[1]:
                last = i
        print(cnt + 2)




