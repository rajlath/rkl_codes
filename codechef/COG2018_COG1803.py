
# -*- coding: utf-8 -*-
# @Date    : 2018-11-23 12:15:30
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
    lens = read_int()
    arrs = read_ints()
    print("NO" if sum(arrs) < 0 else "YES")
