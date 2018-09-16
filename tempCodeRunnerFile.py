
# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 22:13:21
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : http://codeforces.com/contest/1038/problem/C
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

noe = read_int()
list_A = sorted(read_ints() + [0])
list_B = sorted(read_ints() + [0])
sa, sb = 0, 0
while len(list_A) > 1 and len(list_B) > 1:
    if list_A[-1] > list_B[-1]:sa += list_A.pop()
    else:list_B.pop()
    if list_A[-1] > list_B[-1]:list_A.pop()
    else:sb += list_B.pop()
print(sa - sb)
















