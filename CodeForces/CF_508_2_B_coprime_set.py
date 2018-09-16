
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 07:44:33
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://codeforces.com/contest/1038/problem/B
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

noe  = read_int()

if noe > 2:
    print("Yes")
    print(1, noe)
    print(noe-1,*list(range(1, noe)) )
else:
    print("No")

