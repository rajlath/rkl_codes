
# -*- coding: utf-8 -*-
# @Date    : 2018-12-15 20:46:27
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

nb_query = read_int()
for _ in range(nb_query):
    curr = read_int()
    div, rem = divmod(curr, 7)
    ans = div
    if rem == 0: ans = div
    else: ans += 1
    print(ans)




