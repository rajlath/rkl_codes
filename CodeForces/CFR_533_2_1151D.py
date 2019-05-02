
# -*- coding: utf-8 -*-
# @Date    : 2019-04-19 15:39:34
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

nb_students = RI()
line = []
for i in range(nb_students):
    a, b = RMI()
    line.append([(b - a), a, b])
line.sort()
ans = 0
for i in range(nb_students)    :
    ans += i * line[i][1] + (nb_students - i - 1) * line[i][2]
print(ans)
