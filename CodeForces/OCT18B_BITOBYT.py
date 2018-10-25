
# -*- coding: utf-8 -*-
# @Date    : 2018-10-13 08:18:07
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
    _16 = 0
    _8  = 0
    _2  = 0
    n = int(input())
    x = n // 16
    if x > 0:
        _2 += (2 ** x)
    n %= 16
    if n in range(9, 17):
        _16 += 1
    if n in range(3, 9):
        _8  += 1
    else:
        _2 += 1
    print(_2, _8, _16)



