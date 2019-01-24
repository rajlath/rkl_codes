
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 20:20:26
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

nb_Test = read_int()
for _ in range(nb_Test):
    a, b, c, d = read_ints()
    ab = (a + b)//2
    cd = (c + d)//2
    if ab != cd:
        print(ab, cd)
    else:
        if ab + 1 <= b :
            print(ab+1, cd)
        elif ab - 1 >= a:
            print(ab - 1, cd)
        elif cd + 1 <= d:
            print(ab, cd + 1)
        elif cd - 1 >= c:
            print(ab, cd-1)