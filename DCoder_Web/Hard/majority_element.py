'''
Find the majority element in array.
Problem statement
Given an array of n elements containing duplicate elements, your task is to find the majority element. An element is said to be majority if it occures more than n/2 times.
Input
First line of input contains n, no. of elements .
Next line containes n space separated integers, elements of array.
Output
Print the majority element if exist else -1
Constraint
0≤n≤1000
Sample Input
9
3 3 4 2 4 4 2 4 4
Sample Output
4
'''

# -*- coding: utf-8 -*-
# @Date    : 2018-09-12 12:10:35
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

nb_elements = read_int()
arr         = read_ints()
maxs = nb_elements // 2 + 1
counts = {}
ans = -1
for i in arr:
    counts[i] = counts.get(i, 0) + 1
    if counts[i]>= maxs:
        ans = i
        break
print(ans)



