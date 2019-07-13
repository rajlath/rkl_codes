
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 09:04:09
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
    lens = RI()
    sers = RMI()
    diff = 0
    diffs = [ y - x for x, y in zip(sers, sers[1:])]
    diff = diffs[0]
    if diffs[0] != diffs[1]:
        could_be_4 = (sers[3] - sers[0]) // 3
        could_be_3 = sers[3] - sers[2]
        could_be_2 = diffs[1]
        could_be_1 = diffs[0]
        if could_be_3 == could_be_2:
            diff = could_be_2
            sers[0] = sers[1] - diff
        elif could_be_4 == could_be_1:
            diff = could_be_1
            sers[2] = sers[0] + diff
        elif could_be_3  == could_be_4:
            diff = could_be_4
            sers[1] = sers[0] + diff


    #print(diff)
    ans = [sers[0]]
    for i in range(1, lens):
        ans.append(ans[-1] + diff)
    print(*ans)

