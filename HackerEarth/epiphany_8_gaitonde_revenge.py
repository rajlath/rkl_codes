'''
12
abcbbcdefxyz
6
abz 3 1
baz 3 2
abbby 3 2
adef 3 2
abxc 5 2
acdxyz 5 2

'''
# -*- coding: utf-8 -*-
# @Date    : 2018-09-09 21:12:18
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
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

nots = read_int()
series = read_str()
noq    = read_int()
for _ in range(noq):
    needed, k, at_most = read_strs()
    k, at_most = int(k), int(at_most)
    tokens = []
    i = 0
    while i < nots:
        if i+k > nots:
            tokens.append(series[i:])
        else:
            tokens.append(series[i:i+k])
        i += k
    










