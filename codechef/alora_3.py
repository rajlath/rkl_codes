
# -*- coding: utf-8 -*-
# @Date    : 2019-01-20 10:21:56
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
lens , keys = read_ints()
ins = input()
dicts = {}
less  = {}
for i in range(keys):
    a, b = [x for x in input().split()]
    if b < a:
        dicts[a] = b
    else:
        less[a]  = b
for x in less:
    if less[x] in dicts:
        if dicts[less[x]] < x:
            dicts[x] = dicts[less[x]]
ans = ''
for i in ins:
    if i in dicts:
        ans += dicts[i]
    else:
        ans += i
print(ans)





