
# -*- coding: utf-8 -*-
# @Date    : 2018-09-08 10:48:32
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.hackerrank.com/contests/university-codesprint-5/challenges/exceeding-speed-limit
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

speed = read_int()
if speed > 110:
    print( (speed - 90) * 500, "License removed")
elif speed in range(91, 111):
    print( (speed - 90) * 300, "Warning")
else:
    print(0, 'No punishment')





