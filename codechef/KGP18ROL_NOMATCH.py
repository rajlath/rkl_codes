
# -*- coding: utf-8 -*-
# @Date    : 2018-12-17 09:07:01
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


nb_test = int(input())
for _ in range(nb_test):
    lens = read_int()
    arrs = sorted(read_ints())
    left, right = 0, lens - 1
    ans = 0
    while left < right:
        ans += arrs[right] - arrs[left]
        left  += 1
        right -= 1
    print(ans)
