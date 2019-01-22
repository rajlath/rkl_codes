
# -*- coding: utf-8 -*-
# @Date    : 2019-01-20 13:06:33
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
    lens = int(input())
    arrs = read_ints()
    ans  = 0
    for i in range(32):
        count_set_bits = 0
        for j in range(lens):
            if arrs[j] & (1 << i):
                count_set_bits += 1
        subset = ((1 << count_set_bits) - 1)
        subset *= (1 << i)
        ans += subset
    print(ans)


