
# -*- coding: utf-8 -*-
# @Date    : 2018-11-26 07:42:22
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


from collections import defaultdict

lines = defaultdict(int)

nb_wakes = read_int()
for _ in range(nb_wakes):
    nb, *line = read_ints()
    for i in line:
        lines[i] += 1
    for k, v in lines.items():
        if v == nb_wakes:
            print(k, end=" ")
