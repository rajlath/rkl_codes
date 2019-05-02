
# -*- coding: utf-8 -*-
# @Date    : 2019-03-06 19:27:11
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from collections import defaultdict
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


nb_student, nb_school, nb_choosen = RMI()
school_stud = defaultdict(list)

powers = RMI()
schools= RMI()
needs = 0
for i, v  in enumerate(schools):
    if v not in school_stud or powers[i] > powers[school_stud[v]]:
        school_stud[v] = i
count = 0
choosen = RMI()
for i in choosen:
    i -= 1
    if school_stud[schools[i]] != i:
        count += 1
print(count)

