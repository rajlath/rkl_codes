
# -*- coding: utf-8 -*-
# @Date    : 2018-10-19 07:22:47
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

a, b = read_ints()
play_time = 0
while a * b > 1:
    if a > b : a, b = b, a
    play_time += 1
    a  += 1
    b -=  2
    #print(a, b)
print(play_time)
