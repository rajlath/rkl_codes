
# -*- coding: utf-8 -*-
# @Date    : 2019-01-18 19:43:20
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

matrix = [[0 for x in range(1000)] for y in range(1000)]
nb_rectangle = int(input())
total_area = 0
for _ in xrange(nb_rectangle):
    x1, y1, x2, y2 = read_ints()
    for x in range(x1, x2):
        for y in xrange(y1, y2):
            matrix[x][y] += 1
            total_area += matrix[x][y] == 1
print(total_area)
