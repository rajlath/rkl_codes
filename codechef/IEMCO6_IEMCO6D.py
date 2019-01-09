
# -*- coding: utf-8 -*-
# @Date    : 2018-11-12 07:56:34
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


nb_test = read_int()
for _ in range(nb_test):
    lens = read_int()
    strs = [int(x) for x  in input()]
    max_now = 0
    all_max = 0
    for i in strs:
        max_now += [-1, 1][i == 0]
        all_max = max(all_max, max_now)
        if max_now < 0: max_now = 0
    print(-1 if all_max == 0 else all_max)


