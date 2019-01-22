
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 13:28:49
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

nb_elems = read_int()
elem_a   = sorted(read_ints())
elem_b   = sorted(read_ints())
print(sum([abs(x-y) for x, y in zip(elem_a, elem_b)]) % int(10e9 + 7))

