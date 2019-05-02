
# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 22:55:52
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


def countOnes(n):
    if n <= 0 :return 0
    q = n
    x = 1
    ans = 0
    while q > 0:
        digit = q % 10
        q //= 10
        ans += q * x
        if digit == 1: ans += n % x + 1
        if digit > 1: ans += x
        x *= 10
    return ans

nb_test = RI()
for _ in range(nb_test):
    n = RI()
    print(countOnes(n))
