
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 20:11:11
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/ENSE2018/problems/ARGTS2
# @Version : 1.0.0
# adoption of solution by mrbrionix https://www.codechef.com/viewsolution/20077091

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)
mods   = 10 ** 9 + 7

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

def root(x):
    if x not in pa:return x
    else:
        pa[x] = pa.get(x, root(pa[x]))
        print(pa[x])

def merge(x, y):
    x = root(x)
    y = root(y)
    print(x, y)
    if x == y:return
    if x  > y: x, y = y, x
    pa[y] = x



nb_tests = read_int()
for _ in range(nb_tests):
    nb_sites, nb_queries = read_ints()
    for _ in range(nb_queries):
        pa = {}
        comm, a, b = read_ints()
        if comm == 1:
            merge(a, b)
            print(pa)
        else:
            print("YES" if root(a) == root(b) else "NO")