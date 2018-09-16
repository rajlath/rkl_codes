
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 20:18:38
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : http://codeforces.com/contest/1036/problem/A
# @Version : 1.0.0

import os
from sys import stdin
from math import floor, ceil

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

a, b = read_ints()
print((b-1)//a+1)
