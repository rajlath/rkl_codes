
# -*- coding: utf-8 -*-
# @Date    : 2018-09-30 15:05:32
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
    x, y, n, m = read_ints()
    ans = -1
    if x and y : ans = int(abs(x * y)/gcd(x, y))
    print("YES" if x*n>= ans and y*m>=ans else "NO")





