
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 09:22:01
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
ins  = read_str()
ans = "NO"
ans1=''
for i in range(1, lens):
    if ins[i] != ins[i-1]:
        ans = "YES"
        ans1 = ins[i-1:i+1]
        break
print(ans)
if ans1:print(ans1)

