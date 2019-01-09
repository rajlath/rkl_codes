
# -*- coding: utf-8 -*-
# @Date    : 2018-11-12 20:10:45
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


lens = read_int()
strs = read_str()
maxc = max(strs)
ans  = ''
done = False
for i in strs:
    if i == maxc:
        if not done:
            done = True
            continue
    ans += i
print(ans)

