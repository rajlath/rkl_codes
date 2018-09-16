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

nots = read_int()
for _ in range(nots):
    n = read_int()
    a = read_ints()
    b = read_ints()
    even_a, odds_a,even_b, odds_b = [None]*n,[None]*n,[None]*n,[None]*n
    for i, x in enumerate(a):
        if i%2==0: even_a[i] = x
        else: odds_a[i] = x
    for i, x in enumerate(b):
        if i%2==0: even_b[i] = x
        else: odds_b[i] = x
    even_ok = False
    odds_ok = False
    for i in range(len(even_a)):
        if even_a[i:] + even_a[:i] == odds_a or even_a[i:] + even_a[:i] == odds_b:
            even_ok = True
        if odds_a[i:] + odds_a[:i] == even_a or odds_a[i:] + odds_a[:i] == even_b:
            odds_ok = True
        if even_ok and odds_ok:break
    print("Yes" if even_ok and odds_ok else "No")






