
# -*- coding: utf-8 -*-
# @Date    : 2019-03-16 07:50:01
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

Nb_peoples, need = RMI()
people = []
_, *president =  RMI()
for _ in range(Nb_peoples - 1):
    _, *current = RMI()
    people.append(current)
in_family = 1
members   = Counter(president)
to_do = True
while to_do:
    alien = []
    to_do = False
    for i in range(len(people)):
        maybe = 0
        for j in people[i]:
            maybe += j in members
            if maybe >= need:
                in_family += 1
                members += Counter(people[i])
                to_do = True
                break
        else:
            alien.append(people[i])
    people = alien[:]

print(in_family)







