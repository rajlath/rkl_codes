
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 20:11:11
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]
from math import sqrt
nots = read_int()
for _ in range(nots):
    height, distance, j_speed = read_ints()
    gravity = 10
    # height = 0.5 * ( gravity ) * (t * t)
    # time   =  (height / (0.5 * gravity)) ** (0.5)

    time_for_fall = sqrt( height * 2 / gravity)
    time_to_reach = distance / j_speed
    print("Ran away" if time_to_reach <= time_for_fall else "Caught")



