
# -*- coding: utf-8 -*-
# @Date    : 2018-09-08 21:56:08
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.hackerearth.com/challenge/competitive/September-easy-18/algorithm/pair-recovery-f27a26a4/
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

a, b = read_ints()
nexts1 = b - a
nexts2 = a - nexts1
print(nexts2, nexts1)

