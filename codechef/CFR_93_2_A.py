
# -*- coding: utf-8 -*-
# @Date    : 2019-01-22 18:58:14
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



nb_points, ktimes = read_ints()
x, y = read_ints()
distance_sum = 0
for i in range(nb_points-1):
    x1, y1 = read_ints()
    distance_sum += (((x - x1) ** 2 + (y - y1) ** 2)) ** 0.5
    x, y = x1, y1

print("{:.9f}".format(distance_sum * ktimes / 50))