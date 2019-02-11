
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 13:20:52
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


nb_days = int(input())
days    = read_ints()
last    = days[-1]
if last == 15: print("DOWN")
elif last == 0:  print("UP")
elif nb_days == 1:   print(-1)
else:
    if last > days[-2]:
        print("UP")
    else:
        print("DOWN")
