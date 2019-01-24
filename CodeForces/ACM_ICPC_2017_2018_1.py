
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 13:43:42
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


nb_groups = int(input())
classes   = [[x for x in input()] for _ in range(nb_groups)]
print(max([sum([int(x) for x in y]) for y in list(zip(*classes))]))

