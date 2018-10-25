
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

limit = 100001
mods  = 1000000007

def build_series():
    series = [0]
    for i, v in enumerate(range(5, limit, 3)):
        series.append((series[-1] + pow(v, v, mods))%mods)
    return series

nb_test = read_int()
series  = build_series()
for _ in range(nb_test):
    left, rite = read_ints()
    left = max(0, (left // 3) -1)
    rite = (rite - 2 )//3
    resu = series[rite] - series[left]
    if resu < 0: resu += mods
    print(resu)



