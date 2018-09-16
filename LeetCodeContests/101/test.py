
# -*- coding: utf-8 -*-
# @Date    : 2018-09-09 18:49:13
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

A = [3,8,0,9,2,5]
n = len(A)//2
vals = [None] * n
cs   = [None] * n

for i in range(n):
    print(i, i*2 + 1)
    vals[i] = A[i*2+1]
    cs[i]   = A[i*2]
print(vals, cs)
