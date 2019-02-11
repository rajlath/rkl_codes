
# -*- coding: utf-8 -*-
# @Date    : 2019-01-31 13:50:36
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from collections import defaultdict

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

ch = "g"
if ch >="a" and ch < "n":
   print(chr(ord("n") + (ord(ch) - ord("a"))))









