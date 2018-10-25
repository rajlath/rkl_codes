
# -*- coding: utf-8 -*-
# @Date    : 2018-10-17 19:41:42
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

from collections import Counter

alls = Counter(read_ints())
lens = len(alls)
maxs = max(alls.values())
if maxs < 4:
    print("Alien")
elif lens ==  3 or maxs == 5:
    print("Bear")
else:
    print("Elephant")
