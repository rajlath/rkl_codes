
# -*- coding: utf-8 -*-
# @Date    : 2018-11-01 09:17:27
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


def F(s):
    if len(s)%2==1:return s
    s1 = F(s[:len(s)//2])
    s2 = F(s[len(s)//2:])
    if s1 < s2:return s1 + s2
    return s2 + s1
F1 = F(input())
F2 = F(input())
print(["NO", "YES"][F1 == F2])



