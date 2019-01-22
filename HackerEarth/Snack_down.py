
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 13:28:49
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
    total = int(input())
    A_can = read_ints()[1:]
    B_can = read_ints()[1:]
    can_do= list(set(A_can + B_can))
    to_do = list(range(total+1)[1:])
    print(["NO", "YES"][can_do == to_do])
