
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 21:31:07
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import gcd
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


A, B, C, D = map(int, input().split())


def gcd(x, y):
    while x % y > 0:
        x, y = y, x % y
    return y


def lcm(x, y):
    return (x * y) // gcd(x, y)


num1 = B // C - (A - 1) // C
num2 = B // D - (A - 1) // D
num3 = B // lcm(C, D) - (A - 1) // lcm(C, D)


print(B - A + 1 - (num1 + num2 - num3))