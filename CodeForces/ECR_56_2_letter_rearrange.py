
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
    curr = input()
    if curr != curr[::-1]:
        print(curr)
    else:
        ans  = "".join(sorted(curr))
        if ans == curr:
            print(-1)
        else:
            print(ans)






