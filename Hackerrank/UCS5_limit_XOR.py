
# -*- coding: utf-8 -*-
# @Date    : 2018-09-08 10:48:32
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.hackerrank.com/contests/university-codesprint-5/challenges/limit-xor
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

nb_ele, k_fact = read_ints()
elements       = read_ints()

xors = elements[0]
count = 0
left, rite = 0, 0
while rite < nb_ele:
    if xors < k_fact:
        rite += 1
        count += (rite - left)
        if rite < nb_ele:
            xors ^= elements[rite]
    else:
        xors ^= elements[left]
        left += 1
print(count)















