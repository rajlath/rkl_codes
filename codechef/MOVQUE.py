
# -*- coding: utf-8 -*-
# @Date    : 2019-01-28 19:05:36
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


def msbPos(n):
    pos = 0
    while n != 0:
        pos += 1
        n = n >> 1
    return pos

def josephify(n):
    position = msbPos(n)
    j = 1 << (position - 1)
    n = n ^ j
    n = n << 1
    n = n | 1
    return n


nb_test = int(input())
for _ in range(nb_test):
    ins = int(input())
    for i in range(32):
        curr = 1 << i
        if curr > ins:
            break
    print(2 ** (i-1))


