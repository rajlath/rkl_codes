
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 13:53:30
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

def gcd(a, b):
    if b == 0:return a
    return gcd(b, a%b)


nb_test = RI()
for _ in range(nb_test):
    a, b = RMI()
    if a == 0:
        print(b)
    else:
        a1 = 0
        bs = str(b)
        for i in range(len(bs)):
            a1 = a1 * 10 + (int(bs[i]))
            a1 %= a
        print(gcd(a, a1))