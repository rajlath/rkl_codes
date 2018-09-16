'''
2
4
4 4 4 4
4 4 4 4
4
1 2 3 4
3 4 5 2
'''
# -*- coding: utf-8 -*-
# @Date    : 2018-09-09 21:12:18
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

def is_rotated(u, v, k1):
    n, i, j = len(u), 0, 0
    while i < n and j < n:
        k = k1
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += k1
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False

def is_rotated_all(u, v, k1):
    n, i, j = len(u), 0, 0
    while i < n and j < n:
        k = k1
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += 1
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False


nots = read_int()
for _ in range(nots):
    n = read_int()
    a = read_ints()
    b = read_ints()
    ans = "Yes"
    if set(a) != set(b):
        ans = "No"
    else:
        for i in [1,2]:
            if not is_rotated(a, b, i):
                if not is_rotated_all(a, b, 1):
                    ans = "No"
                    break
    print(ans)







