
# -*- coding: utf-8 -*-
# @Date    : 2018-09-29 19:42:53
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
    noi = read_int()
    invalid = 0
    for _ in range(noi):
        a, b  = read_ints()
        invalid += (b - a) > 5
    print(invalid)