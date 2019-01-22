
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 19:29:00
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

n , change = read_ints()
ns = list(str(n))
nsl= len(ns)
c = 0
i = 0
while i < n and change:
    if ns[i] != "9":
        ns[i] = "9"
        change -= 1
    i += 1
print("".join(ns))





