
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 13:43:22
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
    lens = read_int()
    bobs = sorted(read_ints(), reverse=True)
    alic = sorted(read_ints(), reverse=True)
    bob = bobs[0]
    ali = alic[0]
    if bob == ali:
        print("Tie")
    elif bob > ali:
        print("Bob")
    else:
        print("Alice")

