
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 11:44:49
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

nb_letters = read_int()
letter = read_strs()
needs  = read_str()
need   = 0
for i in needs:
    if i in letter:
        letter.pop(letter.index(i))
    else:
        need += 1
print(need)