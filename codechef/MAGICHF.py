
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 15:55:20
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

nb_tests = read_int()
for _ in range(nb_tests):
    nb_box, coin_in, nb_swap = read_ints()
    boxes = {i:0 for i in range(1,nb_box +1)}
    boxes[coin_in] = 1
    for _ in range(nb_swap):
        a, b = read_ints()
        boxes[a], boxes[b] = boxes[b], boxes[a]
    for i in boxes:
        if boxes[i]==1:
            print(i)
            break
