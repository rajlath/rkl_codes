
# -*- coding: utf-8 -*-
# @Date    : 2019-02-24 07:40:03
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


nb_elem = int(input())
elems   = [int(input()) for _ in range(nb_elem)]
for i in range(2, max(elems)):
    if len(set(j%i for j in elems)) == 1:
        print(i, end=" ")
