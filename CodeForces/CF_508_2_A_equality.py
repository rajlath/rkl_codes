
# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 22:13:21
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : http://codeforces.com/contest/1038/problem/A
# @Version : 1.0.0

import os
from sys import stdin
from collections import OrderedDict
from string import ascii_uppercase as uc

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

nb_chr, k = read_ints()
sequence  = read_str()
counts    = {x:0 for x in uc[:k]}
ans = 0
res = []
for i, v in enumerate(sequence):
    counts[v]+= 1
    res.append((i+1, min(counts.values())))
print(res[-1][1] * k)












