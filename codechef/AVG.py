
# -*- coding: utf-8 -*-
# @Date    : 2019-02-23 20:29:34
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
    n, k, v = read_ints()
    remains = read_ints()
    dels, rem = divmod(v * (n + k) - sum(remains), k)
    if rem == 0 and dels > 0:
        print(dels)
    else:
        print(-1)