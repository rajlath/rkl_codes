
# -*- coding: utf-8 -*-
# @Date    : 2018-11-28 09:53:46
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




nb_test = read_int()
for _ in range(nb_test):
    fruits, needed = read_ints()
    costs = sorted(read_ints())
    left = 0
    rite = costs[fruits-1] * needed
    while left < rite:
        mid = (left + rite) // 2
        total = 0
        for i in range(fruits):
            total += (mid // costs[i])
        if total < needed:
            left = mid + 1
        else:rite = mid
    print(rite)




