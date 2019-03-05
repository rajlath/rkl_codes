
# -*- coding: utf-8 -*-
# @Date    : 2019-02-24 09:43:13
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
    locations  = sorted([[int(x) for x in input().split()] for _ in range(int(input()))])
    i = 0
    j = 0
    n = len(locations)
    cnt = 0
    while i < n and j < n:
        j = i + 1
        prev = locations[i][1]
        while j < n and locations[j][0] <= prev:
            prev = min(prev, locations[j][1])
            j += 1
        i = j
        cnt += 1
    print(cnt)
