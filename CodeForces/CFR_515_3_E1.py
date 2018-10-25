
# -*- coding: utf-8 -*-
# @Date    : 2018-10-17 19:41:42
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



MOD = 998244353

n, m = read_ints()
a = read_str()
b = read_str()
ans = 0
x = 0
p = 1
i = m - 1
j = n - 1
while i >= 0:
    if j >= 0:
        x  += (int(a[j]) * p )%MOD
        p  = (p * 2)%MOD
    if b[i] == "1":
        ans = (ans + x) % MOD
    i -= 1
    j -= 1
print(ans)