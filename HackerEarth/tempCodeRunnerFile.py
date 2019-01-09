
# -*- coding: utf-8 -*-
# @Date    : 2018-11-24 08:40:37
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]



import math
def add_no_carry(a, b):
    sums = 0
    res  = 0
    tens = 1
    while (a or b):
       sums = ((a%10) + (b%10))
       sums = sums %10
       res  = (sums * tens) + res
       a = math.floor(a/10)
       b = math.floor(b/10)
       tens = tens * 10
    return res

nb_test = read_int()
for _ in range(nb_test):
    a = read_int()
    b = read_int()
    x = a + b
    print((a + b) - add_no_carry(a, b))




