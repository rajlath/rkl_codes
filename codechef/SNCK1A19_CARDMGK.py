
# -*- coding: utf-8 -*-
# @Date    : 2018-10-20 07:38:09
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
    lens = read_int()
    arrs = read_ints()
    sarr = sorted(arrs)
    arr  = arrs + arrs
    ans  = "NO"
    for i in range(lens):
        if arr[i] == min(arrs):
            if arr[i+lens-1] == max(arrs):
                if arr[i:i+lens] == sarr:
                    ans = "YES"
            break
    print(ans)




