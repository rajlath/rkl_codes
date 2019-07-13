
# -*- coding: utf-8 -*-
# @Date    : 2019-06-15 20:23:26
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


nb_elem = RI()
elements = sorted(RMI())
mins = elements[0]
maxs = elements[-1]
ans = []
for e in elements[1:-1]:
    if e > 0:
        ans.append([mins, e])
        mins -= e
    else:
        ans.append([maxs, e])
        maxs -= e
ans.append([maxs, mins])
print(maxs - mins)
for i in ans:
    print(*i)