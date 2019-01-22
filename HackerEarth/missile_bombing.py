
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 19:12:53
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from collections import Counter

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

matrix = [[0 for x in range(1005)] for y in range(1005)]
nb = int(input())
nb_drop= int(input())
for _ in range(nb_drop):
    p, x1, y1, x2, y2 = read_ints()
    for i in range(x1, x2+1):
        matrix[i][y1] ^= p
        matrix[i][y2+1] ^= p
for i in range(1, nb+1):
    for j in range(1, nb+1):
        matrix[i][j]  = matrix[i][j]^matrix[i][j-1]
        print(matrix[i][j], end= " ")
    print()













