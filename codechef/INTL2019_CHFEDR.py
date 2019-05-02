
# -*- coding: utf-8 -*-
# @Date    : 2019-04-20 13:49:05
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

def get_div(x, factor):
    ret = 0
    while x % factor == 0:
        x //= factor
        ret += 1
    return ret



nb_test = RI()
for _ in range(nb_test):
    v, c = RMI()
    a, b = get_div(abs(v), 5), get_div(abs(c), 2)
    pow1, pow2 = 0, 0
    if c > 0:
        pow1 = pow(abs(v), c, 9)
    else:
        pow1 = pow(2, a * abs(c), 9)
    if v > 0:
        pow2 = pow(abs(c), v, 9)
    else:
        pow2 = pow(5, b * abs(v), 9)
    print(min(pow1, pow2))

