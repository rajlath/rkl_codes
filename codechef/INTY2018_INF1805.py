
# -*- coding: utf-8 -*-
# @Date    : 2018-10-21 18:32:13
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

#learned from solution by huggy_hermit

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]


nb_test = read_int()
for _ in range(nb_test):
    nb_stone, nb_qry = read_ints()
    carrots  = read_ints()
    dp = {i:carrots[0] for i in range(nb_stone+1)}
    for i in range(nb_stone):
        for j in range(i+1, nb_stone, i+1):
            dp[i] += carrots[j]
    for _ in range(nb_qry):
        print(dp[read_int()])


