
# -*- coding: utf-8 -*-
# @Date    : 2018-10-02 08:00:37
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

def dig_total(s):
    return sum([int(x) for x in str(s)])

number = read_str()
lens = len(number)
ans1 = int(number[0]) * 10 ** (lens-1) - 1
ans2  = int(number) - ans1
#print(ans1, ans2)
print(dig_total(ans1) + dig_total(ans2) )


