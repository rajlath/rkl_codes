
# -*- coding: utf-8 -*-
# @Date    : 2018-09-28 09:18:53
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

cups = sum(read_ints())
medal= sum(read_ints())
shelves = read_int()
need = cups//5 + (1 if cups%5>0 else 0)
need += medal//10 + (1 if medal%10>0 else 0)
#print(need)
if shelves >= need:
    print("YES")
else:
    print("NO")



