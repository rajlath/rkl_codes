
# -*- coding: utf-8 -*-
# @Date    : 2019-03-25 07:44:40
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


nb_test = RI()
for _ in range(nb_test):
    score = defaultdict(list)
    for _ in range(12):
        htn, htg, _, atg, atn =RWI()
        htg = int(htg)
        atg = int(atg)
        if not score[htn]:score[htn] = [0, 0]
        if not score[atn]:score[atn] = [0, 0]

        if htg > atg:
            score[htn][0] += 3
        elif htg == atg:
            score[htn][0] += 1
            score[atn][0] += 1
        else:
            score[atn][0] += 3
        score[htn][1] += htg - atg
        score[atn][1] += atg - htg

    score = sorted(score.items(), key =lambda k_v: (k_v[1][0], k_v[1][1]), reverse=True)
    print(score[0][0], score[1][0])


