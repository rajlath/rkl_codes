
# -*- coding: utf-8 -*-
# @Date    : 2018-09-24 19:41:47
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input().strip()
def read_strs()    : return [x for x in stdin.readline().split()]
from collections import Counter
nb_test = read_int()
for _ in range(nb_test):
    s = read_str()
    sc = Counter(s).most_common()
    print(len(s) - sc[0][1])
