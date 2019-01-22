
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 15:08:15
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
    n, x = read_ints()
    done = False
    amt  = 0
    for j in range(500):
        for k in range(1, n+1):
            amt += (n * j) + k
            if amt >= x:
                done = True
                print(k)
                break
        if done:break
