
# -*- coding: utf-8 -*-
# @Date    : 2019-03-30 21:43:46
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
    lens, jumps = RMI()
    points = RMI()
    jump_dict = defaultdict(int)
    #print(points[::jumps])
    done  = [0] * lens
    last_sum = 0
    for i, v in enumerate(points):
        if done[i] == 0:
            jump_dict[i] = sum([x for x in points[i::jumps]])
            last_sum += v
            done[i]  = jump_dict[i]
            print(points[i+jumps:lens:jumps])
            j = i + jumps
            while j < lens:
                done[j]  = jump_dict[i] - last_sum
                last_sum += points[j]
                j += jumps
        print(done)


    print(jump_dict)
    print(max(jump_dict.values()))

