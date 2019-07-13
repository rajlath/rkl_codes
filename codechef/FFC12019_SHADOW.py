
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 10:29:31
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

from math import gcd, ceil, floor
def lcm(a, b):
    return (a * b) // gcd(a, b)

def get_sum(a, l, r)    :
    low, high = ceil(l / a), floor(r / a)
    return  ((high - low + 1) * (((low * a) + (high * a)))) // 2


nb_test = RI()
for _ in range(nb_test):
    a, b, l, r = RMI()
    if r < l: l, r = r, l
    sum_a = get_sum(a, l, r)
    sum_b = get_sum(b, l, r)
    sum_lcm = get_sum(lcm(a, b), l, r)
    answer= sum_a + sum_b
    #print(sum_a, sum_b, sum_lcm, answer)
    loves = ((answer - sum_lcm) % 2 == 0)
    loves += (answer % 2 == 0 or answer % 3 == 0)
    #print(loves)
    if loves == 2: print("TRUE LOVE")
    elif loves == 1: print("LOVE")
    else:print("FAKE LOVE")




