
# -*- coding: utf-8 -*-
# @Date    : 2018-10-13 10:45:50
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



nb_test = read_int()
for _ in range(nb_test):
    L, v, l, r = read_ints()
    laterns = L // v
    lefts = (l - 1) // v
    rites = r // v
    #print(laterns, lefts, rites)
    can_see = laterns +  lefts - rites
    print(can_see)