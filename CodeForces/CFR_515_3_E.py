
# -*- coding: utf-8 -*-
# @Date    : 2018-10-13 10:45:50
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
def add(a, b):
    a += b
    if a < 0: a += MOD
    if a >=MOD: a -= MOD
    return a

len1, len2 = read_ints()
a = read_str()
b = read_str()
pw, res, ans = 1, 0, 0
for i in range(len2):
    if i < len1 and a[len1 - i - 1] == "1":
        res += add(res, pw)
    if (b[len2 - i - 1] == "1"):
        ans = add(ans, res)
print(ans)


