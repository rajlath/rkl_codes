
# -*- coding: utf-8 -*-
# @Date    : 2018-11-01 09:17:27
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


nb_indexes = read_int()
indexes    = [0] * 3001
ins        = read_ints()
for i in ins:
    indexes[i] = 1
print(indexes[1:].index(0) + 1)
