
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 20:20:26
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

import itertools
options = ["".join(i) for i in list(itertools.permutations(["R", "G", "B"]))]

lens = read_int()
ins  = input()
mins = int(10e10)
ansl = mins
ans  = ''
for i in options:
    curr = i * (lens // 3) + i[:lens%3]
    curr_min = sum(1 for x, y in zip(ins, curr) if x != y)
    if curr_min < mins:
        ansl = curr_min
        ans  = curr
        mins = curr_min
print(ansl)
print(ans)


