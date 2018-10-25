
# -*- coding: utf-8 -*-
# @Date    : 2018-10-22 07:11:28
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

def needed(hts):
    maxi = hts.index(max(hts))
    if maxi == 0 or maxi == (len(hts)-1):
        return 1
    else:
        return 1 + min(needed(hts[:maxi]), needed(hts[maxi+1:]))


nb_test = read_int()
for _ in range(nb_test):
    nb_hills = read_int()
    heights  = read_ints()
    print(needed(heights))




