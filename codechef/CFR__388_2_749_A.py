
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

number = read_int()
digits  = number // 2
print(digits)
Answer = ['2'] * (digits-1)
Answer.append(['2', '3'][number - digits*2])
print(*Answer)



