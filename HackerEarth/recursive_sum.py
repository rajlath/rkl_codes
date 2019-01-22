
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 19:12:53
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

def digSum( n):
    sum = 0
    while(n > 0 or sum > 9):
        if(n == 0):
            n = sum
            sum = 0
        sum += n % 10
        n //= 10
    return sum



nb_test = read_int()
for _ in range(nb_test):
    nb_entry = read_int()
    sums = 0
    for _ in range(nb_entry):
        a, b = read_ints()
        sums += a * b
    print(digSum(sums))








