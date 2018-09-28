
# -*- coding: utf-8 -*-
# @Date    : 2018-09-22 09:42:15
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/COW2018/problems/BDMS
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
    angle = read_int()
    print("Yes" if (360 / (180 - angle)) % 1 == 0 else "No")

