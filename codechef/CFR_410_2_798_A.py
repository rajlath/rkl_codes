
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


ins = read_str()
diff= sum([a != b for a, b in zip(ins, ins[::-1])])
if diff == 2 or (diff == 0 and len(ins)%2):
    print("YES")
else:
    print("NO")
