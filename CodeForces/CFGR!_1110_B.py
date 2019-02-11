
# -*- coding: utf-8 -*-
# @Date    : 2019-02-08 08:18:25
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

n, m, k = read_ints()
arr = read_ints()
gaps = sorted([y-x-1 for x, y in zip(arr, arr[1:])])
ans  = arr[-1] - arr[0] + 1 - sum(gaps[n - k:])
print(ans)




