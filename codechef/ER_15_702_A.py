
# -*- coding: utf-8 -*-
# @Date    : 2018-10-24 15:54:39
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


lens = read_int()
arrs = read_ints()
curr  = 0
all_max = 1
maxs = 0
for i in arrs:
    if i > curr:
        maxs += 1
    else:
        maxs = 1
    all_max = max(all_max, maxs)
    curr = i
print(all_max)
