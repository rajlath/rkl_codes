
# -*- coding: utf-8 -*-
# @Date    : 2018-09-08 21:45:46
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin
from math import gcd

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]



nots = read_int()
for _ in range(nots):
    arr = read_ints()
    max_gcd = arr[0]
    max_len = 1
    left , rite = 0, 0
    while rite < len(arr):
        curr = gcd(max_gcd, arr[rite])
        if curr > max_gcd:
            max_gcd = curr
            max_len += 1
     


