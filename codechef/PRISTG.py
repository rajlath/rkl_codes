
# -*- coding: utf-8 -*-
# @Date    : 2018-09-19 22:11:19
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

pats = read_str()
text = read_str()
cnt = 0
m = len(pats)
n = len(text)
for i in range(n-m+1):
    for j in range(m):
        if text[i+j].startswith(pats[j]):
            cnt += 1

print(cnt)



