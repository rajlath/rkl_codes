
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 19:12:53
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from collections import Counter

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb = int(input())
elem = read_ints()
print(sum(elem[::3]), sum(elem[1::3]), sum(elem[2::3]))














