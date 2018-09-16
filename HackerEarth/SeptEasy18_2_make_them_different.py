
# -*- coding: utf-8 -*-
# @Date    : 2018-09-08 21:56:08
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.hackerearth.com/challenge/competitive/September-easy-18/algorithm/make-them-different-5d897ef6/
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
from collections import Counter
nb_elem, remove_cost, reduce_cost = read_ints()
arr = read_ints()
arr = sorted(arr)
uniques = []
for i in arr:
    if i in uniques:
        cnt = 0
        x = i
        while (x-1) in arr[:i] + arr[i+1:]:
            x -= 1
            cnt += 1
        if reduce_cost * cnt < remove_cost:
            total_cost += reduce_cost * cnt
            uniques.append()

        total_cost += min(remove_cost, reduce_cost * cnt)




