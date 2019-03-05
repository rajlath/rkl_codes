# -*- coding: utf-8 -*-
# @Date    : 2019-02-23 15:15:00
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


nb_elements = int(input())
elements = [int(x) for x in input().split()]
elem_sort = sorted(elements)
arrA = []
arrB = []
for i, v in enumerate(elem_sort):
    if i%2==0:
        arrA.append(v)
    else:
        arrB.append(v)
print(*(arrA + arrB[::-1]))