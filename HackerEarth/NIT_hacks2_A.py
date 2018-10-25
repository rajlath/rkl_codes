
# -*- coding: utf-8 -*-
# @Date    : 2018-10-18 18:53:31
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
    src, tgt, limit = read_strs()
    limit = int(limit)
    lens  = len(src)
    mins = max_val
    ans  = ''
    for i in range(lens - limit + 1):
        csrc = src[i:i+limit]
        ctgt = tgt[i:i+limit]
        diff = sum([1 if csrc[x] != ctgt[x] else 0 for x in range(limit)])
        if diff == mins:
            if csrc < ans:
                ans = csrc
        else:
            if diff < mins:
                mins= diff
                ans = csrc
    print(ans)



