
# -*- coding: utf-8 -*-
# @Date    : 2018-10-08 07:48:11
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


from math import gcd
nb_test = read_int()
for _ in range(nb_test):
    lens = read_int()
    arrs = read_ints()
    ands = arrs[0]
    for i in range(1, lens):
        ands &= arrs[i]
    ans =   gcd(ands, 1000000007)
    print([-1, ans][ans == 1])



