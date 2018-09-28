
# -*- coding: utf-8 -*-
# @Date    : 2018-09-16 21:34:21
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

'''
2
5 2 1
5 5 5 5 4
3 3 5
1 2 3
Output:
50
6
'''

import os
from sys import stdin
from functools import reduce

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

nb_tests = read_int()
for _ in range(nb_tests):
    n, k, q = read_ints()
    elements= read_ints()
    if n <= k:
        print(reduce(lambda a, b : a * b, elements))
    else:
        sort_elements = sorted(elements, reverse=True)
        k1 = 0
        for i in range(n):
            a = sort_elements[i]
            ai = 

