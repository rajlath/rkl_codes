
# -*- coding: utf-8 -*-
# @Date    : 2018-09-28 09:18:53
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
nb_round = read_int()
result = 0
for _ in range(nb_round):
    a, b = read_ints()
    result += 1 if a > b else -1 if a < b else 0
print("Mishka" if result > 0 else ["Friendship is magic!^^","Chris"][result<0])


