# -*- coding: utf-8 -*-
# @Date    : 2018-09-03 08:46:01
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : http://codeforces.com/contest/1037/problem/C
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

str_len = read_int()
str_A   = read_str()
str_B   = read_str()

result1 = 0
result2 = 0
index  = 0
while index < str_len-1:
    if str_A[index] not in (str_A[index+1], str_B[index]) and str_B[index] is not str_B[index+1]:
        result += 1
    index += 1
for index in range(str_len):
    result2 += (str_A[index] is not str_B[index])
print( result2 - result1)




