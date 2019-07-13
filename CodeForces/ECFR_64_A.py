
# -*- coding: utf-8 -*-
# @Date    : 2019-05-02 09:45:31
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


nb_figures = RI()
figures = RMI()
infinite = False
touches  = 0
for i in range(nb_figures - 1):
    curr = figures[i] + figures[i+1]
    if curr == 5:
        infinite = True
        break
    else:
        touches += curr
    if i > 0 :
        if figures[i - 1] == 3 and figures[i] == 1 and figures[i + 1] == 2:
            touches -= 1
print("Infinite" if infinite else "Finite" +"\n"+str(touches))


