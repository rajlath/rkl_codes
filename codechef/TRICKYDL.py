
# -*- coding: utf-8 -*-
# @Date    : 2019-02-23 20:40:56
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

values = [pow(2, i-1) for i in range(1, 32)]
#print(values)
nb_test = int(input())
for _ in range(nb_test):
    A = int(input())
    take = 0
    give = 0
    profit = 0
    i = 0
    j = 0
    while take > (give - 1):
            take += A
            give += pow(2, i)
            if take - give > profit:
                    profit = take - give
                    j = i
            i += 1
    print(i-1, j + 1)











