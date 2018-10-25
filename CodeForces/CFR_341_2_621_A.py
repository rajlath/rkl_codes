
# -*- coding: utf-8 -*-
# @Date    : 2018-10-09 20:12:15
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


lens = read_int()
elem = read_ints()
odds, min_odd, sums = 0, max_val, 0
for i in elem:
    sums += i
    if i%2:
        odds =  1 - odds
        min_odd = min(min_odd, i)
print(sums - odds * min_odd)

