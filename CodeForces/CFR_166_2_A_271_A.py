
# -*- coding: utf-8 -*-
# @Date    : 2019-02-08 08:18:25
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

year = int(input())
while year <= 9000:
    year += 1
    if len(set(str(year))) == 4:
        break
if year-1 == 9000:print(9012)
else:print(year)
