
# -*- coding: utf-8 -*-
# @Date    : 2018-11-16 20:33:44
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]


nb_test = read_int()
for _ in range(nb_test):
    a, b, k = read_ints()
    if k % 2 == 0:
        print((a - b) * (k // 2))
    else:
        print((a - b) * (k // 2) + a)