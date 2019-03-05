# -*- coding: utf-8 -*-
# @Date    : 2019-02-23 15:15:00
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

last_x, last_y = 0, 0
nb_moments = int(input())
can_be = 1
for _ in range(nb_moments):
    cur_x,  cur_y =  [int(x) for x in input().split()]
    can_be += max(0, (min(cur_x, cur_y) - max(last_x, last_y) + (last_x != last_y)))
    last_x, last_y = cur_x, cur_y
print(can_be)
