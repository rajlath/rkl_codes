
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 19:12:53
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from collections import Counter

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

import re
nb_lines = int(input())
maxl = 0
maxal= 0
lines= []
cl = 0
for _ in range(nb_lines):
    lines.append(input())
for i, v in enumerate(lines):
    lst = re.findall(r"([C]+)",v)
    if len(lst) > 0:
        maxl = max(maxl,len(max(lst, key= len)))

all_lines = "".join(lines)
print(all_lines)
lst = re.findall(r"([C]+)",all_lines)
maxal = 0
if len(lst) > 0:
    maxal = len(max(lst, key=len))
print(maxl, maxal)















