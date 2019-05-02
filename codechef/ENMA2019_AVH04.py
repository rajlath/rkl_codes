
# -*- coding: utf-8 -*-
# @Date    : 2019-03-30 15:39:41
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


nb_teams = RI()
teams = [[i+1 ,0, 0] for i in range(nb_teams)}
matches = (nb_teams * ( nb_teams - 1)) // 2
for _ in range(matches):
    t1, t2, g1, g2 = RMI()
    if g1 > g2:
        teams[t1][0] += 4
        teams[t1][1] += (g2 - g1)
        teams[t2][1] += (g1 - g2)
    elif g1 == g2:
        teams[t1][0] += 1
        teams[t1][1] += (g2 - g1)
        teams[t2][1] += (g1 - g2)
        teams[t2][0] += 1
    else:
        teams[t2][0] += 4
        teams[t2][1] += (g2 - g1)
        teams[t1][1] += (g1 - g2)
teams = sorted(teams.values(), key = lambda x: (x[0], -x[1]), reverse = True)
print(teams)
