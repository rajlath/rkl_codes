
# -*- coding: utf-8 -*-
# @Date    : 2019-01-18 20:33:39
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


nb_test = int(input())
for _ in range(nb_test):
    prev , nexts = 0, 0
    ins = input()
    for i in ins:
        temp = nexts
        nexts= ord(i) - ord('a')
        prev = temp
        if nexts - prev <= -13:
            print(nexts - prev + 26, end = " ")
        elif nexts - prev > 13:
            print(nexts - prev - 26, end = " ")
        else:
            print(nexts - prev, end = " ")

