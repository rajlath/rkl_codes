
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 20:11:11
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/ENSE2018/problems/CHFWV
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)
mods   = 10 ** 9 + 7

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

def prepare_arr(arr):
    arr.sort()
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def max_even(arr):
    max_curr = 0
    max_alls = 0
    for i in range(len(arr)):
        if not arr[i]%2:
            max_curr += 1
        else:
            max_alls= max(max_alls, max_curr)
            max_curr = 0
    return max(max_alls, max_curr)

nots = read_int()
for _ in range(nots):
    lens = read_int()
    arrs = read_ints()
    arrs = prepare_arr(arrs)
    print(max_even(arrs))





