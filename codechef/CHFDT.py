
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 19:35:04
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

nb_times, lens = read_ints()
original = input()
min_wrong = 100
ans = ''
for _ in range(nb_times):
    sents  = input()
    wrongs = sum([1 for x, y in zip(original, sents) if x != y])
    pc_err = (wrongs / len(sents) ) * 100
    if pc_err < min_wrong:
        ans = sents
print(ans)


