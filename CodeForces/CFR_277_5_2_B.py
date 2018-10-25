
# -*- coding: utf-8 -*-
# @Date    : 2018-09-29 09:04:10
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

nb_boys = read_int()
boys    = sorted(read_ints())
nb_girl = read_int()
girls   = sorted(read_ints())
pairs   = 0
while boys and girls:
    if abs(boys[-1] - girls[-1]) <= 1:
        pairs += 1
        boys.pop()
        girls.pop()
    elif boys[-1] > girls[-1]:
        boys.pop()
    else:
        girls.pop()
print(pairs)



