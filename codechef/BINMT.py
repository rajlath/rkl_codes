
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 20:11:11
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/ENSE2018/problems/BINMT/
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nots = read_int()
for _ in range(nots):
    nb_mats = read_int()
    mats = [[int(x) for x in input().split()] for y in range(nb_mats)]
    #rows = [[True if mats[x][y] == 0 else False for y  in range(nb_mats)] for x in range(nb_mats)]
    rows = [False] * nb_mats
    cols = [False] * nb_mats
    for i in range(nb_mats):
        for j in range(nb_mats):
            if mats[i][j] == 0:
                rows[i] = True
                cols[j] = True

    for i in range(nb_mats):
        for j in range(nb_mats):
            if rows[i] or cols[j]:print("0", end=" ")
            else: print("1", end=" ")
        print()





