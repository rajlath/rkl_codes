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

lasta = 0
lastb = 0
nb_moments = int(input())
count = 1
for _ in range(nb_moments):
    cura, curb = read_ints()
    maxs = (cura, curb)
    for i in range()


print(count)