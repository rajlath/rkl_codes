
# -*- coding: utf-8 -*-
# @Date    : 2019-01-22 18:58:14
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



nb_balls = int(input())
sizes = sorted(set(read_ints()))
ans = "NO"
if len(sizes) >= 3:
    for i in range(len(sizes)-2):
        if sizes[i+2] == sizes[i+1]+1 == sizes[i] + 2:
            ans = "YES"
            break
print(ans)


ans = "NO"
for size in sizes:
    if size+1 in sizes and size+2 in sizes:
        ans = "YES"
        break
print(ans)