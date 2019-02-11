
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 20:43:43
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


nb_bags, total, multiple = read_ints()
x = 1
while  True:
    curr = multiple * x
    total -= curr
    if total < (x + 1)*multiple:break
    else: x += 1
print(nb_bags - x)