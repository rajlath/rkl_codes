
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

s = read_str()
ab= s.find("AB")
ba= s.find("BA")
if (ab != -1 and s.find("BA", ab+2)>-1) or (ba != -1 and s.find("AB", ba+2)>-1):
    print("YES")
else:
    print("NO")
