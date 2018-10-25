
# -*- coding: utf-8 -*-
# @Date    : 2018-09-30 15:05:32
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
for _ in range(read_int()):
    n, m = read_ints()
    book = read_ints()
    left = read_ints()
    rite = read_ints()
    limit = max(rite) + 1
    beg = [0] * (limit)
    end = [0] * (limit)
    for x in book:
        beg[x] += 1
        end[x] += x
    begs = list(accumulate(beg))
    ends = list(accumulate(end))

    for i in range(n):
        print(begs[rite[i]] - begs[left[i] - 1], ends[rite[i]] - ends[left[i] - 1])








