
# -*- coding: utf-8 -*-
# @Date    : 2018-11-19 21:41:13
# @Author  :  (oorja.halt@gmail.com)
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
    x, n = read_ints()
    ans = 0
    for i in range(0, n):
        if i%x == 0:
            ans += i
    print(ans)

