
# -*- coding: utf-8 -*-
# @Date    : 2018-10-24 15:54:39
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


wa = read_str()
wb = read_str()
print("-1" if wa == wb else max(len(wa), len(wb)))