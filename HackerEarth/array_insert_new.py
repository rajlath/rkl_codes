
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 19:12:53
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

nb_elements, nb_query = read_ints()
elements = read_ints()
for _ in range(nb_query):
    m, x, y = read_ints()
    if m == 1:
        elements[x] = y
    if m == 2:
        if x >= 0 and y <= nb_elements:
            sums = 0
            for i in range(x, y+1):
                sums += elements[i]
            print(sums)



