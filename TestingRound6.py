
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 11:58:54
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


nb_candies, nb_friends = read_ints()
div, mod = divmod(nb_candies, nb_friends)
distribute = [div] * nb_friends
for i in range(1, mod+1):
    distribute[-i] += 1
print(*distribute)