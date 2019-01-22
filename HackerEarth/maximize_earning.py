
# -*- coding: utf-8 -*-
# @Date    : 2019-01-20 16:18:07
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


nb_street = read_int()
for _ in range(nb_street):
    nb_building, amount = read_ints()
    heights = read_ints()
    earning = amount
    high    = heights[0]
    for i in heights[1:]:
        earning += amount * (i > high)
        if i > high:high = i
    print(earning)