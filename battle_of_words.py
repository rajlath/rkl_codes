
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 19:12:53
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from itertools import accumulate

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_element, nb_query = read_ints()
elements = [0] + list(accumulate(read_ints()))
for _ in range(nb_query):
    l, r = read_ints()

    print((elements[r] - elements[l-1]) // (r - l + 1))








