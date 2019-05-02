
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 22:14:16
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
    candies, nb_frnd, k =  RMI()
    throws  = 0
    thrown = 0
    ans = 0
    while True:
        curr = candies - thrown
        if curr <= 0:
            ans = -1
            break
        if curr % nb_frnd == 0:
            break
        thrown += k
        ans += 1
    print(ans)


