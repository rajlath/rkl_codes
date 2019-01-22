
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 20:07:43
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


lens = int(input())
elem = read_ints()
sums = list(accumulate(elem))
nb_qry = int(input())
for i in range(nb_qry):
    lower, upper  = read_ints()
    lower-=1
    upper-=1
    ones = sums[upper] if lower == 0 else sums[upper] - sums[lower - 1]
    print(ones %2, upper - lower + 1 - ones)



