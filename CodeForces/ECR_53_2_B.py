
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 08:46:22
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
p = {x:i for i, x in enumerate(read_ints()) }
i = -1
ans = []
for x in read_ints():
    j = max(i, p[x])
    ans += j - i,
    i = j
print(*ans)
