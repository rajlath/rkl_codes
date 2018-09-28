
# -*- coding: utf-8 -*-
# @Date    : 2018-09-24 19:29:03
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/NPLQ2018/problems/NPLQ18F
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

from string import ascii_lowercase as lc

nb_test = read_int()
for _ in range(nb_test):
    s = read_str()
    alpha = {a:0 for a in lc}
    maxs = 0
    for i in s:
        alpha[i] += 1
        maxs = max(alpha[i], maxs)
    print(alpha)
    print(len(s) - maxs)






